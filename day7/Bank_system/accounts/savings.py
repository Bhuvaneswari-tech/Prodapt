from accounts.base_account import BankAccount
from accounts.exceptions import InsufficientFundsError

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        interest = self.balance * 0.04  # 4% interest
        return(f"Interest earned: {interest:.2f}")
    
    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientFundsError(self.balance,amount)
        self.balance-=amount
        print(f"Withdraw {amount}. New Balance: {self.balance}")