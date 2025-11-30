import unittest
from programming_paradigm.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_deposit(self):
        acc = BankAccount(0)
        acc.deposit(50)
        self.assertEqual(acc.balance, 50.0)

    def test_withdraw_success(self):
        acc = BankAccount(100)
        self.assertTrue(acc.withdraw(40))
        self.assertEqual(acc.balance, 60.0)

    def test_withdraw_insufficient(self):
        acc = BankAccount(30)
        self.assertFalse(acc.withdraw(50))
        self.assertEqual(acc.balance, 30.0)

    def test_negative_deposit_raises(self):
        acc = BankAccount(0)
        with self.assertRaises(ValueError):
            acc.deposit(-10)

    def test_negative_withdraw_raises(self):
        acc = BankAccount(50)
        with self.assertRaises(ValueError):
            acc.withdraw(-20)

    def test_initial_negative_raises(self):
        with self.assertRaises(ValueError):
            BankAccount(-1)

if __name__ == "__main__":
    unittest.main()
