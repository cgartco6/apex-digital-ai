import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app

def save_uploaded_file(file):
    """Save uploaded file to the uploads folder"""
    if not file:
        return None
        
    # Create unique filename
    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4().hex}_{filename}"
    
    # Create uploads directory if not exists
    upload_dir = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_dir, exist_ok=True)
    
    # Save file
    file_path = os.path.join(upload_dir, unique_filename)
    file.save(file_path)
    
    return unique_filename
