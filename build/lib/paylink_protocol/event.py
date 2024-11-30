class Event:
    def __init__(self, app_id, purchased_token, purchase_amount, user_id, customer_user_address):
        self.app_id = app_id
        self.purchased_token = purchased_token
        self.purchase_amount = purchase_amount
        self.user_id = user_id
        self.customer_user_address = customer_user_address

    def __str__(self):
        return f"Event(app_id={self.app_id}, purchased_token={self.purchased_token}, purchase_amount={self.purchase_amount}, user_id={self.user_id}, customer_user_address={self.customer_user_address})"
