import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@localhost/apex_digital')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # 24 hours
    
    # Payment Gateway Configuration
    PAYMENT_GATEWAY_URL = os.getenv('PAYMENT_GATEWAY_URL', 'https://api.paymentgateway.co.za/v1/transactions')
    PAYMENT_API_KEY = os.getenv('PAYMENT_API_KEY', 'your_api_key')
    
    # Email Configuration
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.afrihost.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SMTP_USER = os.getenv('SMTP_USER', 'info@apex-digital.co.za')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'your_email_password')
    
    # AI Configuration
    AI_API_KEY = os.getenv('AI_API_KEY', 'your_openai_api_key')
    AI_MODEL = os.getenv('AI_MODEL', 'gpt-4')
    
    # File Storage
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB
    
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'super-secret-key')
