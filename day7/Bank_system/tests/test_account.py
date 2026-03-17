import unittest
from accounts.current import CurrentAccount
from accounts.savings import SavingsAccount
from accounts.exceptions import InsufficientFundsError

class TestBankAccounts(unittest.TestCase):
    def setUp(self):
        self.savings =  SavingsAccount("Alice",1000)
        self.current = CurrentAccount("Bob", 2000)
        
    def test_savings_interest(self):
        expected_interest = 1000 * 0.04
        self.assertEqual(expected_interest,40.00)
        
    def test_current_interest(self):
        initial_balance = self.current.balance
        self.current.calculate_interest()
        self.assertEqual(self.current.balance,initial_balance)
    
    def test_inheritance_info(self):
        self.assertEqual(self.savings.owner,"Alice")
        self.assertEqual(self.current.owner,"Bob")
    
    def test_insufficient_funds(self):
        acc = SavingsAccount("Alice",100)
        with self.assertRaises(InsufficientFundsError):
            acc.withdraw(500)
        
if __name__=="__main__":
    unittest.main()