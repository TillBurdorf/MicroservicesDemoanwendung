from flask import Flask, jsonify, request

# Initialisierung der Flask App
app = Flask(__name__)

# Beispielhafte Produktdaten
products = {
    "1": {"name": "Laptop", "inventory": 10},
    "2": {"name": "Smartphone", "inventory": 20},
    "3": {"name": "FlatScreen", "inventory": 10},
}

# Definiert einen API Endpunkt /products für GET anfragen
@app.route('/products', methods=['GET'])
def get_products():
    # der aktuelle Lagerbestand wird im JSON Format ausgegeben
    return jsonify(products)

# Definiert einen API Endpunkt /reduce_inventory für POST anfragen
@app.route('/reduce_inventory', methods=['POST'])
def reduce_inventory():
    # Liest die Produkt-ID und die Menge aus der Anfrage
    product_id = request.json.get("product_id")
    quantity = request.json.get("quantity", 1)  # Standardmäßig 1

    # Überprüft, ob das Produkt existiert und genügend Lagerbestand vorhanden ist
    if product_id in products and products[product_id]["inventory"] >= quantity:
        products[product_id]["inventory"] -= quantity # das Produkt mit der übergebenen Produkt ID wird im Bestand reduziert
        return jsonify({"message": "Inventory updated"}), 200 # Erfolgsmeldung und senden des Statuscode 200 
    else:
        return jsonify({"error": "Insufficient inventory"}), 400 # Fehlermeldung und Statuscode 400

# Start der Flask App auf dem Port 5001
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)