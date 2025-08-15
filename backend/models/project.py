from datetime import datetime
from .. import db

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    service = db.Column(db.String(50), nullable=False)
    package = db.Column(db.String(20), nullable=False)  # starter, professional, enterprise
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, in_progress, testing, completed, delivered
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    
    ai_agents = db.relationship('AIAgent', backref='project', lazy=True)
    
    def __repr__(self):
        return f'<Project {self.code}>'
