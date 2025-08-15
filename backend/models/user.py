from datetime import datetime
from .. import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    company = db.Column(db.String(100))
    role = db.Column(db.String(20), default='client')  # client, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    projects = db.relationship('Project', backref='user', lazy=True)
    payments = db.relationship('Payment', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.email}>'
