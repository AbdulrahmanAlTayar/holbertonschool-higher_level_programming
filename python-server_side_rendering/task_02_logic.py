from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items_page():
    # Read JSON file
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"items": []}
    
    items_list = data.get("items", [])
    
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

