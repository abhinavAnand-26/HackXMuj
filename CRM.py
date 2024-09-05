class Scooter:
    def __init__(self, manufacturer, current_location, status):
        self.manufacturer = manufacturer
        self.current_location = current_location
        self.status = status  # 0: Manufacturer, 1: Bikesetu Yard, 2: Franchise Store, 3: End Customer

class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        # Add other customer fields if needed

# Implement CRM Functionality
customers = []
num_customers = 0

def add_customer(customer):
    global num_customers
    customers.append(customer)
    num_customers += 1

def get_customer_by_id(customer_id):
    for customer in customers:
        if customer.customer_id == customer_id:
            return customer
    # Handle customer not found
    return None  # or raise an exception

# Integrate CRM with Tracking System
def get_customer_id_for_scooter(scooter_id):
    # Placeholder function: implement logic to get customer_id based on scooter_id
    pass

def update_customer_purchase_history(customer_id, scooter_id):
    # Placeholder function: implement logic to update the customer's purchase history
    pass

def update_scooter_status(scooter_id, new_status):
    # Update scooter status logic here
    # ...

    # Update customer information if necessary
    if new_status == 3:  # Scooter sold to end customer
        customer_id = get_customer_id_for_scooter(scooter_id)
        update_customer_purchase_history(customer_id, scooter_id)
