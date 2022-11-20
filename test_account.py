'''
Account testing module
'''

import pytest
from account import Account

class Test:
    '''
    Test class
    '''

    # Setup and teardown

    def setup_method(self):
        '''
        Create our test Account objects
        '''
        self.a_1 = Account('Foo')
        self.a_2 = Account('Bar')

    def teardown_method(self):
        '''
        Delete our test Account objects
        '''
        del self.a_1
        del self.a_2

    # Tests

    def test_init(self):
        '''
        Tests account initalization.
        Accounts should have a name and balance of 0.
        '''
        assert self.a_1.get_name() == 'Foo'
        assert self.a_1.get_balance() == pytest.approx(0, abs=0.001)

        assert self.a_2.get_name() == 'Bar'
        assert self.a_2.get_balance() == pytest.approx(0, abs=0.001)

    def test_deposit(self):
        '''
        Test deposits
        '''
        # Basic functionality
        assert self.a_1.get_balance() == pytest.approx(0, abs=0.001)
        assert self.a_1.deposit(5) is True
        assert self.a_1.get_balance() == pytest.approx(5, abs=0.001)
        assert self.a_1.deposit(10.0) is True
        assert self.a_1.get_balance() == pytest.approx(15.0, abs=0.001)

        # Ensure accounts aren't at all connected.
        assert self.a_2.get_balance() == pytest.approx(0, abs=0.001)
        assert self.a_1.deposit(10) is True
        assert self.a_2.get_balance() == pytest.approx(0, abs=0.001)

        # Return false if negative, 0
        assert self.a_1.deposit(-1) is False
        assert self.a_1.deposit(0) is False

        # Check incompatible type
        with pytest.raises(TypeError):
            self.a_1.deposit('Zero')

    def test_withdraw(self):
        '''
        Test withdrawals
        '''
        # Basic functionality
        assert self.a_1.get_balance() == pytest.approx(0, abs=0.001)
        assert self.a_1.deposit(5) is True
        assert self.a_1.get_balance() == pytest.approx(5, abs=0.001)
        assert self.a_1.withdraw(5) is True
        assert self.a_1.get_balance() == pytest.approx(0, abs=0.001)

        assert self.a_1.deposit(10.0) is True
        assert self.a_1.withdraw(5) is True
        assert self.a_1.get_balance() == pytest.approx(5.0, abs=0.001)

        # Ensure accounts aren't at all connected.
        assert self.a_2.get_balance() == pytest.approx(0, abs=0.001)
        assert self.a_1.deposit(10) is True
        assert self.a_1.withdraw(5) is True
        assert self.a_2.get_balance() == pytest.approx(0, abs=0.001)

        # Return false if negative, 0, greater than account balance
        assert self.a_2.withdraw(-1) is False
        assert self.a_2.withdraw(0) is False
        assert self.a_2.withdraw(1) is False # Account balance should currently be 0, so we are withdrawing more than the account has at this point.

        # Check incompatible type
        with pytest.raises(TypeError):
            self.a_1.withdraw('Zero')
