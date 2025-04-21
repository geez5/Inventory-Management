from app import app, db
from models import Product
with app.app_context():
    products = Product.query.all()
    for p in products:
        print(p.name, p.quantity)