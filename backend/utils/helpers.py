import random
import string
from datetime import datetime

def generate_project_code():
    """Generate a unique project code"""
    timestamp = datetime.now().strftime("%y%m%d")
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"APX-{timestamp}-{random_str}"
