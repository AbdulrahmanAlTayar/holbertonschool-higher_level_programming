from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# JSON reader
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

# CSV reader
def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# SQLite reader
def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
    return products

@app.route('/products')
def products_page():
    source = request.args.get("source")
    product_id = request.args.get("id")
    error = None
    products = []

    # Select data source
    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    elif source == "sql":
        products = read_sql()
    else:
        error = "Wrong source"

    # Filter by id if provided
    if not error and product_id:
        try:
            pid = int(product_id)
            filtered = [p for p in products if p['id'] == pid]
            if filtered:
                products = filtered
            else:
                error = "Product not found"
        except ValueError:
            error = "Invalid id"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
