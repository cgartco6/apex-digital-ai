from datetime import datetime
from .. import db

class Payment(db.Model):
    __tablename__ = 'payments'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), default='ZAR')
    transaction_id = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, completed, failed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Distribution details
    ai_upgrade = db.Column(db.Float)
    reserve_fund = db.Column(db.Float)
    owner_revenue = db.Column(db.Float)
    distributed_at = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'<Payment {self.transaction_id}>'
