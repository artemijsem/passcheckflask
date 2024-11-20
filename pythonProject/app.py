from flask import Flask, request, jsonify

app = Flask(__name__)

# Set the correct password (in a real app, store this securely, e.g., hashed in a database)
CORRECT_PASSWORD = "secure123"


@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.json
    if not data or 'password' not in data:
        return jsonify({"success": False, "message": "Password missing"}), 400

    if data['password'] == CORRECT_PASSWORD:
        return jsonify({"success": True, "message": "Access granted"})
    else:
        return jsonify({"success": False, "message": "Incorrect password"}), 403



if __name__ == '__main__':
    app.run(host='passcheckflask-production.up.railway.app', port=5000)

