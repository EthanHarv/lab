'''
Module for "Account" class
'''

class Account:
    '''
    Class to represent account details (name, balance)
    '''

    def __init__(self, name: str) -> None:
        '''
        Account constructor to initalize an account object.
        :param name: Client's name.
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Adds money to account
        :param amount: The amount of money to deposit
        '''
        # Cannot deposit 0 or negative amount
        if amount <= 0:
            return False

        self.__account_balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        '''
        Withdraws money from account
        :param amount: The amount of money to withdraw
        '''
        # Cannot withdraw 0, negative amount, or more than is held.
        if amount <= 0 or amount > self.__account_balance:
            return False

        self.__account_balance -= amount
        return True

    def get_balance(self) -> float:
        '''
        Returns account balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Returns account name
        '''
        return self.__account_name
