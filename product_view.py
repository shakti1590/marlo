from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product data (replace this with your data source)
products = [
    {'id': 1, 'name': 'Product 1', 'price': 200, 'rating': 4.5},
    {'id': 2, 'name': 'Product 2', 'price': 100, 'rating': 3.8},
    # ... other products ...
]

@app.route('/get_products', methods=['GET'])
def get_products():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 5
    sorted_products = sort_products_by_review()
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    paged_products = sorted_products[start_index:end_index]
    return jsonify({'products': paged_products})

def sort_products_by_review():
    sorted_products = sorted(products, key=lambda x: x['rating'], reverse=True)
    return sorted_products

if __name__ == '__main__':
    app.run(debug=True)
