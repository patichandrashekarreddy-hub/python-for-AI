# helpers.py

def calculate_total(quantity, price):
    """Calculate total for a single item"""
    return quantity * price
#not pointless
def format_currency(amount):
    """Format number as for  the currency"""
    return f"${amount:,.3f}"

print(format_currency(1234.567)) the