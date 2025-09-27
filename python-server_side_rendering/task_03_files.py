from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert price and id to proper types
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
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
