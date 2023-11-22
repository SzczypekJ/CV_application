from enum import Enum


class Bank_account:
    def __init__(self, money_in_the_bank=0) -> None:
        self.money_in_the_bank = money_in_the_bank

    def add_money_to_bank(self, amount=0):
        the_number_of_money = int(
            input("Tell me how much money you want to add to the Bank Account: "))
        self.money_in_the_bank += the_number_of_money
        return self.money_in_the_bank

    def get_money_from_bank(self, amount=0):
        the_number_of_money = int(
            input("Tell me how much money you want to get from the Bank Account: "))
        self.money_in_the_bank -= the_number_of_money
        return self.money_in_the_bank

    def __str__(self) -> str:
        return "You have " + str(self.money_in_the_bank) + " money in the bank"
