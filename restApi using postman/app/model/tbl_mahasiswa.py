from app import db
from datetime import datetime

class tbl_mahasiswa(db.Model):
    npm = db.Column(db.String(10), primary_key=True)
    nama = db.Column(db.String(230), nullable=False)
    tgl_lahir = db.Column(db.String(230), nullable=False)
    alamat = db.Column(db.String(230), nullable=False)
    
    def __repr__(self):
        return '<Product {}>'.format(self.nama)