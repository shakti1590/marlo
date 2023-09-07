from flask import Flask, request, jsonify

app = Flask(__name__)

product_reviews = {}

@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.get_json()
    product_id = data.get('product_id')
    review_text = data.get('review_text')
    rating = data.get('rating')
    # Store the review and rating for the product
    if product_id in product_reviews:
        product_reviews[product_id].append({'review': review_text, 'rating': rating})
    else:
        product_reviews[product_id] = [{'review': review_text, 'rating': rating}]
    return jsonify({'message': 'Review submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
