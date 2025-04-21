from app import app, db
from models import Product
from datetime import datetime, timedelta

try:
    with app.app_context():
        db.drop_all()
        db.create_all()

        products = [
            Product(
                name="Milk",
                quantity=30,
                expiration_date=datetime.today() + timedelta(days=5),
                sales_last_30_days=15
            ),
            Product(
                name="Bread",
                quantity=15,
                expiration_date=datetime.today() + timedelta(days=3),
                sales_last_30_days=20
            ),
            Product(
                name="Butter",
                quantity=20,
                expiration_date=datetime.today() + timedelta(days=10),
                sales_last_30_days=10
            ),
            Product(
                name="Eggs",
                quantity=50,
                expiration_date=datetime.today() + timedelta(days=14),
                sales_last_30_days=25
            ),
            Product(
                name="Juice",
                quantity=12,
                expiration_date=datetime.today() + timedelta(days=4),
                sales_last_30_days=8
            )
        ]

        db.session.add_all(products)
        db.session.commit()

        print("✅ Database seeded with sample products!")
except Exception as e:
    print(f"❌ Error seeding database: {str(e)}")