from flask import request
from app import db
from app.model.user import User
from app import response, app

def index():
    try:
        users = User.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        

def transform(users):
    array = []
    for i in users:
        array.append({
            'id': i.id,
            'name': i.name,
            'email': i.email,
        })
    return array

def show(id):
    try:
        users = User.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Empty....')
        
        
        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        
def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email,
    }
    
    return data

def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        
        user = User(name=name, email=email)
        user.setPassword(password)
        db.session.add(user)
        db.session.commit()
        
        return response.ok('', 'Successfully create user!')
    
    except Exception as e:
        print(e)
        return response.bad_request([], 'Failed to create user!')
    
def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        
        user = User.query.filter_by(id=id).first()
        user.name = name
        user.email = email
        user.setPassword(password)
        
        db.session.commit()
        
        return response.ok('', 'Successfully update data!')
    
    except Exception as e:
        print(e)
        return response.bad_request([], 'Failed to update data!')

def delete(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.bad_request([], 'Empty....')
        
        db.session.delete(user)
        db.session.commit()
        
        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        print(e)
        return response.bad_request([], 'Failed to delete data!')