from flask import Flask, jsonify

# Initialisierung der Flask App
app = Flask(__name__)

# Beispielhafte Benutzerdaten
users = {
    "1": {"name": "Manuel Mustermann", "email": "m.mustermann@example.com"},
    "2": {"name": "Manuela Musterfrau", "email": "m.musterfrau@example.com"},
    "3": {"name": "Dirk Divers", "email": "d.divers@example.com"}
}

@app.route('/listUsers', methods=["GET"])
def listUsers():
    return jsonify(users)

# Definiert einen API Endpunkt /user/<user_id> für GET anfragen
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    # Gibt die Benutzerdaten für die angegebene user_id zurück
    user = users.get(user_id)
    if user:
        return jsonify(user), 200 # Erfolg mit Statuscode 200
    else:
        return jsonify({"error": "User not found"}), 404 # Fehler mit Statuscode 404

# Start der Flask App auf dem Port 5003 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)