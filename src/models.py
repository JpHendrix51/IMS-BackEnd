from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)

    def serialize(self):
        return {
            "id":self.id,
            "item": self.item,
            "description": self.description,
            "quantity": self.quantity
        }