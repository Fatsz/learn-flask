from app import app
from flask import request
from app.controller import UserController, ProductController, MahasiswaController

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()

@app.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    else:
        return UserController.delete(id)
    
@app.route('/products', methods=['POST', 'GET'])
def products():
    if request.method == 'GET':
        return ProductController.index()
    else:
        return ProductController.store()

@app.route('/products/<id>')
def productsDetail(id):
    print(id)
    return ProductController.show(id)


@app.route('/mahasiswa', methods=['POST', 'GET', 'PUT'])
def mahasiswa():
    if request.method == 'GET':
        return MahasiswaController.index()
    elif request.method == 'POST':
        return MahasiswaController.store()
    elif request.method == 'PUT':
        return MahasiswaController.update()
    else:
        return MahasiswaController.delete()