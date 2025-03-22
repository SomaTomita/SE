# Abstraction Example
# BAD PRACTICE:
# - Exposing complex payment processing details
# - Direct handling of sensitive data
# - Mixed responsibilities


class BadPaymentProcessor:
    def process_payment(self, amount, card_number, cvv, expiry):
        # Directly exposing all payment processing steps
        self.validate_card(card_number, cvv, expiry)
        self.connect_to_payment_gateway()
        self.encrypt_data()
        self.send_payment_request()
        self.handle_response()
        self.update_transaction_history()
        self.send_confirmation_email()


# GOOD PRACTICE:
# - Hides complex payment processing
# - Clear separation of concerns
# - Simple interface for users
# - Secure handling of sensitive data


class PaymentProcessor:
    def __init__(self):
        self._payment_gateway = PaymentGateway()
        self._notification_service = NotificationService()
        self._transaction_manager = TransactionManager()

    def process_payment(self, payment_details):
        """
        Simple interface for payment processing
        Hides all complexity behind a single method
        """
        try:
            self._payment_gateway.validate_payment(payment_details)
            transaction = self._payment_gateway.execute_payment(payment_details)
            self._transaction_manager.record_transaction(transaction)
            self._notification_service.send_confirmation(transaction)
            return {"success": True, "transaction_id": transaction.id}
        except PaymentError as e:
            self._handle_payment_error(e)


class PaymentGateway:
    def validate_payment(self, payment_details):
        self._check_card_validity()
        self._verify_funds()
        self._assess_risk()

    def execute_payment(self, payment_details):
        self._establish_secure_connection()
        self._process_transaction()
        return Transaction()


class NotificationService:
    def send_confirmation(self, transaction):
        self._prepare_template()
        self._send_email()


class TransactionManager:
    def record_transaction(self, transaction):
        self._save_to_database()
        self._update_audit_log()


if __name__ == "__main__":
    # Client code only needs to know about process_payment
    processor = PaymentProcessor()
    payment_details = {
        "amount": 100.00,
        "currency": "USD",
        "payment_method": "credit_card",
        "card_token": "encrypted_token",
    }
    result = processor.process_payment(payment_details)
