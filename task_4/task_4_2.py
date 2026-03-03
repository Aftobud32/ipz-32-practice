from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]
next_id = 3

def make_response(status, data=None, message=""):
    return jsonify({"status": status, "data": data, "message": message})

@app.route('/users', methods=['GET'])
def get_users():
    return make_response("success", users, "Users retrieved successfully")

@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    if not data or 'name' not in data:
        return make_response("error", None, "Invalid data"), 400
    
    new_user = {
        "id": next_id,
        "name": data['name'],
        "email": data.get('email', '')
    }
    users.append(new_user)
    next_id += 1
    return make_response("success", new_user, "User created"), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return make_response("success", user, "User found")
    return make_response("error", None, "User not found"), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return make_response("error", None, "User not found"), 404
    
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return make_response("success", user, "User updated")

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return make_response("error", None, "User not found"), 404
    
    users = [u for u in users if u['id'] != user_id]
    return make_response("success", None, "User deleted")

if __name__ == '__main__':
    app.run(debug=True, port=5000)