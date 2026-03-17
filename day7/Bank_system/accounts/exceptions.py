class InsufficientFundsError(Exception):
    """Exception raised when a withdrawal exceeds the available balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Withdrawal of {amount} failed. Balance is only {balance}."
        super().__init__(self.message)