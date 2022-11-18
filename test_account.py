'''
Account testing module
'''

import unittest
from account import Account

class TestAccount(unittest.TestCase):
    '''
    Tests
    '''

    delta = 0.000001

    def setUp(self):
        '''
        Create our test Account objects
        '''
        self.account_1 = Account('Foo')
        self.account_2 = Account('Bar')

    def test_init(self):
        '''
        Tests account initalization.
        Accounts should have a name and balance of 0.
        '''
        self.assertEqual(self.account_1.get_name(), 'Foo')
        self.assertEqual(self.account_1.get_balance(), 0)

        self.assertEqual(self.account_2.get_name(), 'Bar')
        self.assertEqual(self.account_2.get_balance(), 0)

    def test_deposit(self):
        '''
        Test deposits
        '''
        # Basic functionality
        self.assertEqual(self.account_1.get_balance(), 0)
        self.assertTrue(self.account_1.deposit(5))
        self.assertEqual(self.account_1.get_balance(), 5)
        self.assertTrue(self.account_1.deposit(10.0))
        self.assertAlmostEqual(self.account_1.get_balance(), 15.0, delta=self.delta)

        # Ensure accounts aren't at all connected.
        self.assertEqual(self.account_2.get_balance(), 0)
        self.assertTrue(self.account_1.deposit(10))
        self.assertEqual(self.account_2.get_balance(), 0)

        # Return false if negative, 0
        self.assertFalse(self.account_1.deposit(-1))
        self.assertFalse(self.account_1.deposit(0))

        # Check incompatible type
        self.assertRaises(TypeError, self.account_1.deposit, 'Zero')

    def test_withdraw(self):
        '''
        Test withdrawals
        '''
        # Basic functionality
        self.assertEqual(self.account_1.get_balance(), 0)
        self.assertTrue(self.account_1.deposit(5))
        self.assertEqual(self.account_1.get_balance(), 5)
        self.assertTrue(self.account_1.withdraw(5))
        self.assertEqual(self.account_1.get_balance(), 0)

        self.assertTrue(self.account_1.deposit(10.0))
        self.assertTrue(self.account_1.withdraw(5))
        self.assertAlmostEqual(self.account_1.get_balance(), 5.0, delta=self.delta)

        # Ensure accounts aren't at all connected.
        self.assertEqual(self.account_2.get_balance(), 0)
        self.assertTrue(self.account_1.deposit(10))
        self.assertTrue(self.account_1.withdraw(5))
        self.assertEqual(self.account_2.get_balance(), 0)

        # Return false if negative, 0, greater than account balance
        self.assertFalse(self.account_2.withdraw(-1))
        self.assertFalse(self.account_2.withdraw(0))
        self.assertFalse(self.account_2.withdraw(1))

        # Check incompatible type
        self.assertRaises(TypeError, self.account_1.withdraw, 'Zero')

if __name__ == "__main__":
    unittest.main()
