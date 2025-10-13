from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class Admin(db.Model, UserMixin):

    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    products = db.relationship('Product', backref='admin', lazy=True)
    posts = db.relationship('Post', backref='admin', lazy=True)

    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.set_password(password)

    def set_password(self, password):

        self.password = generate_password_hash(password)

    def check_password(self, password):

        return check_password_hash(self.password, password)
    
class Product(db.Model):

    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name_product = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))

    def __repr__(self):
        
        return f"Product('{self.name_product}', '{self.price}', '{self.description}', '{self.category}')"

class Post(db.Model):

    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    name_post = db.Column(db.String(100), nullable=False)
    post = db.Column(db.Text, nullable=False)
    date = db.Column(db.String, nullable=False, default=lambda: datetime.utcnow().strftime('%Y-%m-%d'))
    category = db.Column(db.String(100), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))

    def __repr__(self):

        return f"Blog('{self.name_post}', '{self.post}', '{self.date}')"

