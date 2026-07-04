from flask import Flask, request, jsonify

app = Flask(__name__)

# ye list baraye zakhire darooha
drug_list = []

# dictionary baraye mojoodi
inventory = {}

# -------------------------
# login user
# -------------------------

@app.route("/login", methods=["POST"])
def login():

    data = request.json

    user = data.get("username")
    password = data.get("password")

    if user == "admin" and password == "1234":
        return jsonify({"result": "ok"})
    else:
        return jsonify({"result": "error"})


# -------------------------
# ezafe kardan daroo
# -------------------------

@app.route("/addDrug", methods=["POST"])
def add_drug():

    data = request.json

    code = data.get("code")
    name = data.get("name")
    expire = data.get("expire")
    quantity = data.get("quantity")

    drug = {
        "code": code,
        "name": name,
        "expire": expire
    }

    drug_list.append(drug)

    # sabte mojoodi
    inventory[code] = quantity

    return jsonify({"message": "drug added"})


# -------------------------
# namayesh mojoodi
# -------------------------

@app.route("/getInventory", methods=["GET"])
def get_inventory():

    return jsonify(inventory)


# -------------------------
# check kardane kambood daroo
# -------------------------

@app.route("/checkAlerts", methods=["GET"])
def check_alert():

    alerts = []

    for code in inventory:

        if inventory[code] < 100:
            alerts.append(code)

    return jsonify({"low_stock": alerts})


# -------------------------

if __name__ == "__main__":
    app.run(debug=True)
