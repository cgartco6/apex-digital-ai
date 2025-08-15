from datetime import datetime
from .. import db

class AIAgent(db.Model):
    __tablename__ = 'ai_agents'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='assigned')  # assigned, active, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AIAgent {self.role}>'
