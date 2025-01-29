from flask import request
from app import db
from app.model.tbl_mahasiswa import tbl_mahasiswa
from app import response, app

def index():
    try:
        mahasiswa = tbl_mahasiswa.query.all()
        data = transform(mahasiswa)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        
def transform(mahasiswa):
    array = []
    for i in mahasiswa:
        array.append({
            'npm': i.npm,
            'nama': i.nama,
            'tgl_lahir': i.tgl_lahir,
            'alamat': i.alamat,
        })
    return array

def show(npm):
    try:
        mahasiswa = tbl_mahasiswa.query.filter_by(npm=npm).first()
        if not mahasiswa:
            return response.badRequest([], 'Empty....')
        
        
        data = singleTransform(mahasiswa)
        return response.ok(data, "")
    except Exception as e:
        print(e)
    
def singleTransform(mahasiswa):
    data = {
        'npm': mahasiswa.npm,
        'nama': mahasiswa.nama,
        'tgl_lahir': mahasiswa.tgl_lahir,
        'alamat': mahasiswa.alamat,
    }
    
    return data

def store():
    try:
        npm = request.json['npm']
        nama = request.json['nama']
        tgl_lahir = request.json['tgl_lahir']
        alamat = request.json['alamat']
        
        mahasiswa = tbl_mahasiswa(npm=npm, nama=nama, tgl_lahir=tgl_lahir, alamat=alamat)
        db.session.add(mahasiswa)
        db.session.commit()
        
        return response.ok('', 'Successfully create mahasiswa!')
    
    except Exception as e:
        print(e)
        
        return response.badRequest([], 'Failed to create mahasiswa!')

def update():
    try:
        npm = request.json['npm']
        nama = request.json['nama']
        tgl_lahir = request.json['tgl_lahir']
        alamat = request.json['alamat']
        
        mahasiswa = tbl_mahasiswa.query.filter_by(npm=npm).first()
        mahasiswa.npm = npm
        mahasiswa.nama = nama
        mahasiswa.tgl_lahir = tgl_lahir
        mahasiswa.alamat = alamat
        
        db.session.commit()
        
        return response.ok('', 'Successfully update mahasiswa!')
    
    except Exception as e:
        print(e)
        
        return response.badRequest([], 'Failed to update mahasiswa!')

def delete(npm):
    try:
        mahasiswa = tbl_mahasiswa.query.filter_by(npm=npm).first()
        if not mahasiswa:
            return response.badRequest([], 'Empty....')
        
        db.session.delete(mahasiswa)
        db.session.commit()
        
        return response.ok('', 'Successfully delete mahasiswa!')
    except Exception as e:
        print(e)
        
        return response.badRequest([], 'Failed to delete mahasiswa!')