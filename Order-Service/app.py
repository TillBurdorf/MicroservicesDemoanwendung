from flask import Flask, jsonify, request
import requests

# Initialisierung der Flask App 
app = Flask(__name__)

# Definiert einen API Endpunkt /order für POST anfragen
@app.route('/order', methods=['POST'])
def create_order():
    order_data = request.json # Daten der Order im JSON-Format 
    product_id = order_data.get("product_id") # Produkt-ID des bestellten Produktes
    quantity = order_data.get("quantity", 1) # Anzahl der bestellten Produkte mit 1 als default 
    user_id = order_data.get("user_id") # ID des Benutzers, der die Bestellung aufgibt 

    # Anfrage an den Product-Service, um den Lagerbestand zu aktualisieren:
    # über request wird eine API-Anfrage an den /reduce_inventory Endpunkt der Product-Service gestellt.
    # Der Endpunkt erhält als Übergabe eine product_id und die quantity und verringert 
    # dann im Product Service den aktuellen Lagerbestand  
    response = requests.post("http://product-service:5001/reduce_inventory", json={
        "product_id": product_id,
        "quantity": quantity
    })

    # Wenn der Product - Service als Statuscode 200 zurücksendet war die Anfrage erfolgreich
    if response.status_code == 200:
        # Benachrichtigung an den Notification-Service senden, dass die Order erfolgreich war
        requests.post("http://notification-service:5004/notify", json={"user_id": user_id})
        return jsonify({"message": "Order placed successfully"}), 200
    else:
        # Fall für einen Fehler im Product Service, und dem damit verbundenen Status Code 400
        return jsonify({"error": "Failed to place order"}), 400

# Start der Flask App auf dem Port 5002 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)