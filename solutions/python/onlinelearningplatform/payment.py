from datetime import datetime


class Payment:
    def __init__(self, payment_id: str, user_id: str, amount: float, payment_method: str, payment_date: datetime):
        self.payment_id = payment_id
        self.user_id = user_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_date = payment_date
