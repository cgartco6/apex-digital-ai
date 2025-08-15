import requests
from .. import app
from ..models.payment import Payment
from datetime import datetime

def process_payment(data):
    """Process payment using the payment gateway"""
    # In a real implementation, this would connect to a payment gateway
    # For demo purposes, we'll simulate a successful payment
    
    # Simulate payment processing
    amount = data['amount']
    print(f"Processing payment of R{amount} for order")
    
    # Payment gateway request would look like:
    # headers = {"Authorization": f"Bearer {app.config['PAYMENT_API_KEY']}"}
    # payload = {
    #     "amount": amount * 100,  # in cents
    #     "currency": "ZAR",
    #     "customer": data['email'],
    #     "description": f"{data['package']} package for {data['service']}"
    # }
    # response = requests.post(app.config['PAYMENT_GATEWAY_URL'], json=payload, headers=headers)
    
    # For demo, simulate success
    return {
        "success": True,
        "transaction_id": f"PAY-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "amount": amount,
        "message": "Payment processed successfully"
    }

def distribute_funds(amount):
    """Distribute funds according to the specified percentages"""
    # 20% for AI upgrades
    ai_upgrade = amount * 0.2
    # 20% for reserve funds
    reserve = amount * 0.2
    # 60% for owner
    owner = amount * 0.6
    
    print(f"Funds distributed: AI Upgrade: R{ai_upgrade:.2f}, Reserve: R{reserve:.2f}, Owner: R{owner:.2f}")
    return {
        "ai_upgrade": ai_upgrade,
        "reserve_fund": reserve,
        "owner_revenue": owner
    }
