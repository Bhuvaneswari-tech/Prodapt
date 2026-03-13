'''Use Case 1 — ATM Withdrawal System
Scenario:A bank ATM allows only 3 attempts for entering the correct PIN.

Requirements
Ask the user to enter the PIN.
Allow only 3 attempts.
If the correct PIN is entered, allow withdrawal.
Otherwise block the card.
'''

correct_pin = "1234"
attempts = 0

while attempts < 3:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == correct_pin:
        print("Login successful.")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN.")
    
else:
    print("Card blocked.")