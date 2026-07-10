from flask import Flask, jsonify, request

#  (Models) 
# In model-ha baraye negahdari data hastan
class Drug:
    def __init__(self, code, name, quantity):
        self.code = code
        self.name = name
        self.quantity = quantity

#   Services 

# Singleton Pattern baraye Authentication
class AuthenticationService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AuthenticationService, cls).__new__(cls)
            cls._instance.user = "admin"
            cls._instance.password = "1234"
        return cls._instance

    def login(self, user, password):
        return user == self.user and password == self.password

# Inventory Manager (Logic Layer)
class InventoryManager:
    def __init__(self):
        self.drugs = {} # Dictionary baraye zakhire darooha
    
    def add_drug(self, code, name, qty):
        self.drugs[code] = Drug(code, name, qty)
        
    def get_all(self):
        return [{"code": d.code, "name": d.name, "qty": d.quantity} for d in self.drugs.values()]

# Alert Service (Observer)
class AlertService:
    def check_low_stock(self, inventory_manager):
        alerts = []
        for drug in inventory_manager.drugs.values():
            if drug.quantity < 20: # Hade aghal 20
                alerts.append(f"Alert: {drug.name} is low (Stock: {drug.quantity})")
        return alerts

#  App Initialization 
app = Flask(__name__)
inv_manager = InventoryManager()
auth_service = AuthenticationService()
alert_service = AlertService()

# API Routes (Presentation Layer) 

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if auth_service.login(data.get('user'), data.get('pass')):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Wrong credentials"}), 401

@app.route('/add_drug', methods=['POST'])
def add():
    data = request.json
    inv_manager.add_drug(data['code'], data['name'], data['qty'])
    return jsonify({"message": "Drug added"}), 201

@app.route('/inventory', methods=['GET'])
def get_inv():
    return jsonify(inv_manager.get_all())

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alert_service.check_low_stock(inv_manager))

if __name__ == '__main__':
    app.run(debug=True)
