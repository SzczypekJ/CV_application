from result import OK, Error

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """Here is something, which checking the money are real"""

        self.balance += amount

    def try_withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            return OK("You withdraw the cash", amount)
        return Error("You dont have enough money in the Bank", amount)

    def __str__(self):
        return str(self.balance)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, MinimumBalance=1000):
        super().__init__(balance)
        self.MinimumBalance = MinimumBalance

    def try_withdraw(self, amount):
        if self.balance - amount > self.MinimumBalance:
            return super().try_withdraw(amount)
        else:
            return Error("After operation you will have not enough money MinimumBalance", amount)
