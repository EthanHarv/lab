class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        # Cannot deposit 0 or negative amount.
        if amount <= 0:
            return False

        self.__account_balance += amount
        return True

    def withdraw(self, amount):
        # Cannot withdraw 0, negative amount, or more than is held.
        if amount <= 0 or amount > self.__account_balance:
            return False

        self.__account_balance -= amount
        return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
