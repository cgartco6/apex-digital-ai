import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import render_template
from .. import app

def send_email(to, subject, template, **kwargs):
    """Send email using SMTP with HTML template"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = app.config['SMTP_USER']
        msg['To'] = to
        msg['Subject'] = subject
        
        # Render HTML template
        html_content = render_template(f'email/{template}.html', **kwargs)
        
        # Add HTML body
        msg.attach(MIMEText(html_content, 'html'))
        
        # Connect to server and send
        with smtplib.SMTP(app.config['SMTP_SERVER'], app.config['SMTP_PORT']) as server:
            server.starttls()
            server.login(app.config['SMTP_USER'], app.config['SMTP_PASSWORD'])
            server.send_message(msg)
        
        print(f"Email sent to {to}")
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False
