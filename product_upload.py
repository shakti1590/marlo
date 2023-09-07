from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload_products', methods=['POST'])
def upload_products():
    # Your product upload API code here
    uploaded_file = request.files['file']
    # Process the uploaded file
    return jsonify({'message': 'Product upload successful'})

if __name__ == '__main__':
    app.run(debug=True)
