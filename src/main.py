"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db

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

@app.route('/purchases/add')
def purchasesAdd():
    return jsonify([{
        "id": "666",
        "item": "product_1",
        "description": "the first desc",
        "qty": "10"
    }]), 200

@app.route('/products/all')
def productsAll():
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

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
