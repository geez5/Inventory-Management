from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from models import db, Product
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)  # Enable CORS for all routes
db.init_app(app)

# Ensure database tables are created
with app.app_context():
    db.create_all()

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/product/<string:product_name>')
def get_product_info(product_name):
    print(f"Searching for product: {product_name}")
    product = Product.query.filter_by(name=product_name.title()).first()
    if not product:
        print("Product not found")
        return jsonify({'error': 'Product not found'}), 404

    days_remaining = (product.expiration_date - datetime.today()).days
    avg_daily_sales = product.sales_last_30_days / 30 if product.sales_last_30_days else 0
    estimated_days_until_empty = product.quantity / avg_daily_sales if avg_daily_sales else float('inf')
    suggested_quantity = 0

    if estimated_days_until_empty < 7:
        suggested_quantity = max(int(avg_daily_sales * 14) - product.quantity, 0)

    response = {
        "name": product.name,
        "quantity": product.quantity,
        "sold_last_month": product.sales_last_30_days,
        "expiring_soon": days_remaining < 7,
        "needs_restock": product.quantity < 10,
        "estimated_days_until_empty": round(estimated_days_until_empty, 1),
        "suggested_quantity": suggested_quantity
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)