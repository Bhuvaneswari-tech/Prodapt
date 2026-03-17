from accounts.base_account import BankAccount

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current account does not earn interest")
        
