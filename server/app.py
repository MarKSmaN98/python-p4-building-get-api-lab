#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    return_list = []
    for business in Bakery.query.all():
        bak = {
            'id' : business.id,
            'name' : business.name,
            'created_at' : business.created_at
        }
        return_list.append(bak)

    response = make_response(
        return_list,
        200,
        {"Content-Type": "application/json"}
    )
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bak = Bakery.query.filter(Bakery.id == id).first()
    ret = {
        'id':bak.id,
        'name':bak.name,
        'created_at':bak.created_at
    }
    response = make_response(
        ret,
        200,
        {"Content-Type": "application/json"}
    )
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    return_list = []
    for goods in BakedGood.query.order_by(BakedGood.price).all():
        good = {
            'id' : goods.id,
            'name' : goods.name,
            'created_at' : goods.created_at,
            'price':goods.price
        }
        return_list.append(good)

    response = make_response(
        return_list,
        200,
        {"Content-Type": "application/json"}
    )
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    bak=BakedGood.query.order_by(db.desc(BakedGood.price)).first()
    good = {
        'id' : bak.id,
        'name' : bak.name,
        'created_at' : bak.created_at,
        'price':bak.price
    }

    response = make_response(
        good,
        200,
        {"Content-Type": "application/json"}
    )
    return response

if __name__ == '__main__':
    app.run(port=555, debug=True)
