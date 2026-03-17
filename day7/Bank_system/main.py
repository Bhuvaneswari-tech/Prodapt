from accounts.current import CurrentAccount
from accounts.savings import SavingsAccount
from accounts.exceptions import InsufficientFundsError

def run_banking_system():

    with open("transaction_report.txt","w") as report:  
        #wrap your login in a helper to easily write to a file  
        def log(message):
            print(message) #display the output in vscode
            report.write(message+ "\n") #save to the file
        
        log("=== BANKING SYSTEM LOG ===")
        # Create a savings account and calculate interest
        savings_acc = SavingsAccount("Alice", 1000)
        savings_acc.display_info()
        log(f"Initial Balance: {savings_acc.balance}")

        try:
            log("\nAttempting to withdraw 1500 from Alicia's account:")
            savings_acc.withdraw(1500)
        except InsufficientFundsError as e:
            log(f"Bank error: {e}")
        
        interest = savings_acc.calculate_interest()
        log(f"Interest Processed: {interest}")
            
        # Create a current account and calculate interest
        log("Program continues...")
        current_acc = CurrentAccount("Bob", 2000)
        log(f"Account Created: {current_acc.owner}")
        current_acc.display_info()
        log(f"Current Account Balance: {current_acc.balance}")
        current_acc.calculate_interest()
    
if __name__ == "__main__":
    run_banking_system()
    print("\n[Success] All results have been uploaded to 'transaction_report.txt")
