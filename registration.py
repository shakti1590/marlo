from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    # Process the registration data and add user to the list
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        # ... other user details ...
    }
    users.append(new_user)
    return jsonify({'message': 'Registration successful'})

if __name__ == '__main__':
    app.run(debug=True)
