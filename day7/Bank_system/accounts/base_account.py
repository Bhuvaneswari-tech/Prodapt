from abc import ABC, abstractmethod
from datetime import datetime

class BankAccount(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    #abstract method
    @abstractmethod
    def calculate_interest(self):
        pass
    
    #normal method
    def display_info(self):
        print("\n" + "="*30)
        print("GLOBAL NEST BANK STATEMENT")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
        print(f"Account Holder: {self.owner}")
        print("="*30)
    