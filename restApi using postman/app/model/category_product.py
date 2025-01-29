from app import db
from datetime import datetime
from app.model.product import Product

class Category_product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    category = db.Column(db.String(140), nullable=False)
    product_id = db.Column(db.BigInteger, db.ForeignKey('product.id'))
    
    def __repr__(self):
        return '<Category_product {}>'.format(self.category)