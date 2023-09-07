from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    # ... other users ...
]

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Invalid credentials'})

if __name__ == '__main__':
    app.run(debug=True)
