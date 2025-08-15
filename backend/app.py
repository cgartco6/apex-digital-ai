from flask import Flask, jsonify, request, send_from_directory
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from dotenv import load_dotenv
import os
from datetime import timedelta
from models import db
from models.user import User
from models.project import Project
from models.payment import Payment
from models.ai_agent import AIAgent
from services.payment_service import process_payment, distribute_funds
from services.ai_service import create_ai_team, execute_task, monitor_system
from services.email_service import send_email
from utils.security import hash_password, verify_password
from utils.helpers import generate_project_code

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Health check endpoint
@app.route('/')
def health_check():
    return jsonify({"status": "healthy", "message": "Apex Digital AI Backend Running"})

# User Authentication Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = hash_password(data['password'])
    
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        phone=data.get('phone'),
        company=data.get('company'),
        role='client'
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created successfully"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or not verify_password(data['password'], user.password):
        return jsonify({"message": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify({
        "access_token": access_token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    })

# Project Management Routes
@app.route('/api/projects', methods=['POST'])
@jwt_required()
def create_project():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    project = Project(
        code=generate_project_code(),
        user_id=user_id,
        service=data['service'],
        package=data['package'],
        description=data['description'],
        status='pending'
    )
    
    db.session.add(project)
    db.session.commit()
    
    # Create AI team
    ai_team = create_ai_team(data['service'], data['package'])
    
    # Add AI agents to project
    for agent in ai_team:
        new_agent = AIAgent(
            project_id=project.id,
            role=agent['role'],
            status='assigned'
        )
        db.session.add(new_agent)
    
    db.session.commit()
    
    return jsonify({
        "message": "Project created successfully",
        "project_id": project.id,
        "project_code": project.code
    }), 201

@app.route('/api/projects', methods=['GET'])
@jwt_required()
def get_projects():
    user_id = get_jwt_identity()
    projects = Project.query.filter_by(user_id=user_id).all()
    
    return jsonify([{
        "id": p.id,
        "code": p.code,
        "service": p.service,
        "package": p.package,
        "status": p.status,
        "created_at": p.created_at.isoformat()
    } for p in projects])

# Payment Processing
@app.route('/api/payments', methods=['POST'])
@jwt_required()
def create_payment():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    # Process payment
    payment_result = process_payment(data)
    
    if payment_result['success']:
        # Create payment record
        payment = Payment(
            user_id=user_id,
            amount=data['amount'],
            currency='ZAR',
            transaction_id=payment_result['transaction_id'],
            status='completed'
        )
        
        db.session.add(payment)
        db.session.commit()
        
        # Distribute funds
        distribution = distribute_funds(data['amount'])
        
        return jsonify({
            "message": "Payment processed successfully",
            "payment_id": payment.id,
            "distribution": distribution
        }), 201
    else:
        return jsonify({"message": payment_result['message']}), 400

# Dashboard Endpoints
@app.route('/api/dashboard/stats', methods=['GET'])
@jwt_required()
def dashboard_stats():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if user.role != 'admin':
        return jsonify({"message": "Unauthorized"}), 403
    
    # Get revenue stats
    total_revenue = db.session.query(db.func.sum(Payment.amount)).scalar() or 0
    monthly_revenue = db.session.query(db.func.sum(Payment.amount)).filter(
        db.func.extract('month', Payment.created_at) == db.func.extract('month', db.func.now())
    ).scalar() or 0
    
    # Get project stats
    total_projects = Project.query.count()
    active_projects = Project.query.filter(Project.status.in_(['in_progress', 'testing'])).count()
    
    return jsonify({
        "total_revenue": total_revenue,
        "monthly_revenue": monthly_revenue,
        "total_projects": total_projects,
        "active_projects": active_projects
    })

# Admin Endpoints
@app.route('/api/admin/users', methods=['GET'])
@jwt_required()
def admin_users():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if user.role != 'admin':
        return jsonify({"message": "Unauthorized"}), 403
    
    users = User.query.all()
    return jsonify([{
        "id": u.id,
        "name": u.name,
        "email": u.email,
        "company": u.company,
        "created_at": u.created_at.isoformat()
    } for u in users])

# System Management
@app.route('/api/system/monitor', methods=['POST'])
def system_monitor():
    monitor_system()
    return jsonify({"message": "System monitoring completed"})

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
