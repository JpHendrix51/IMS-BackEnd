"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Products

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

########################################### FOR THE PURCHASES TABLE ################################################

# TO ADD A NEW RECORD ON THE PURCHASES TABLE

@app.route('/purchases/add')
def purchasesAdd():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

# TO REMOVE A RECORD FROM THE PURCHASES TABLE

@app.route('/purchases/remove/<int:purchases_id>')
def purchasesRemove():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

######################################### FOR THE TRANSACTIONS_PIVOT TABLE ################################################

# TO GET ALL PURCHASES FROM THE TRANSACTIONS TABLE BASED ON AN ID:

@app.route('/transactions/purchases/<int:purchases_id>')
def transactionsPurchasesGet():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

# TO DELETE A RECORD ON THE TRANSACTIONS TABLE RELATED TO A PURCHASE BASED ON A PURCHASE ID:
# FOR EXAMPLE AN ITEM ADDED IN A PURCHASE RECORD

@app.route('/transactions/purchases/remove/<int:transactions_id>')
def transactionsPurchasesRemove():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

# TO GET ALL SALES FROM THE TRANSACTIONS TABLE BASED ON AN ID:

@app.route('/transactions/sales/remove/<int:transactions_id>')
def transactionsSalesGet():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

# TO DELETE A RECORD ON THE TRANSACTIONS TABLE RELATED TO A SALE BASED ON A SALE ID:
# FOR EXAMPLE AN ITEM ADDED IN A SALE RECORD

@app.route('/transactions/sales/remove/<int:sales_id>')
def transactionsSalesRemove():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200


# TO GET ALL THE DELIVERIES FROM THE TRANSACTIONS TABLE:

@app.route('/transactions/deliveries')
def transactionsDeliveriesGet():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

# TO GET A SINGLE DELIVERY FROM THE TRANSACTIONS TABLE BASED ON AN ID:

@app.route('/transactions/delivery/<int:delivery_id>')
def transactionsDeliveryGet():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

########################################### FOR THE SALES TABLE ################################################

# TO ADD A NEW RECORD ON THE SALES TABLE

@app.route('/sales/add')
def salesAdd():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

# TO REMOVE A RECORD FROM THE SALES TABLE

@app.route('/sales/remove/<int:purchases_id>')
def salesRemove():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

########################################### FOR THE DELIVERIES TABLE ################################################

# TO ADD A NEW RECORD ON THE DELIVERIES TABLE

@app.route('/deliveries/add')
def deliveriesAdd():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

# TO ADD A NEW RECORD FROM THE DELIVERIES TABLE

@app.route('/deliveries/remove/<int:deliveries_id>')
def deliveriesRemove():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

# TO GET A PARTICULAR LOCATION FROM A RECORD IN THE DELIVERIES TABLE

@app.route('/deliveries/map/<int:deliveries_id>')

def deliveriesMap():

    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

########################################### FOR THE PRODUCTS TABLE ################################################

# TO GET ALL PRODUCTS FROM THE PRODUCTS/INVENTORY TABLE

@app.route('/products/all/beta', methods=['POST', 'GET'])

def productsAllGetBeta():
    #     body = request.get_json()

    #     if body is None:
    #         raise APIException("You need to specify the request body as a json object", status_code=400)
    #     if 'item' not in body:
    #         raise APIException('You need to specify the item', status_code=400)
    #     if 'description' not in body:
    #         raise APIException('You need to specify the description', status_code=400)
    #     if 'quantity' not in body:
    #         raise APIException('You need to specify the quantity', status_code=400)

    if request.method == 'POST':
        for i in range(20):
            p = Products(item=f'item{i}', description=f'description{i}')
            db.session.add(p)

        db.session.commit()

        all_products = Products.query.all()
        all_products = list(map(lambda item: item.serialize(), all_products))
        return jsonify(all_products), 200

    # GET request
    if request.method == 'GET':
        all_products = Products.query.all()
        all_products = list(map(lambda item: item.serialize(), all_products))
        return jsonify(all_products), 200

    return "Invalid Method", 404

@app.route('/products/all')

def productsAllGet():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    },
    {
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    },
    {
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

# TO GET A PARTICULAR PRODUCT FROM THE PRODUCTS/INVENTORY TABLE

@app.route('/products/<int:products_id>')

def productsSingleGet():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200




# @app.route('/purchases/add')
# def purchasesAdd():
#     return jsonify([{
#         "id": "666",
#         "item": "product_1",
#         "description": "the first desc",
#         "qty": "10"
#     }]), 200

#

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
