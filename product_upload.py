from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload_products', methods=['POST'])
def upload_products():
    uploaded_file = request.files['file']
    return jsonify({'message': 'Product upload successful'})

if __name__ == '__main__':
    app.run(debug=True)
