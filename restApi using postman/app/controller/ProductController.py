from flask import request
from app.model.product import Product
from app import response, app
from app import db

def index():
    try:
        products = Product.query.all()
        data = transform(products)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def transform(products):
    array = []
    for i in products:
        array.append({
            'id': i.id,
            'name': i.name,
            'price': i.price,
        })
    return array

def show(id):
    try:
        products = Product.query.filter_by(id=id).first()
        if not products:
            return response.bad_request([], 'Empty...')
        
        data = singleTransform(products)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        
def singleTransform(products):
    data = {
        'id': products.id,
        'name': products.name,
        'price': products.price
    }
    
    return data

def store():
    try:
        name = request.json['name']
        price = request.json['price']
        
        products = Product(name=name, price=price)
        db.session.add(products)
        db.session.commit
        
        return response.ok('', 'Successfully create data!')
    
    except Exception as e:
        print(e)
    
