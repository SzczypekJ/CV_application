from bankaccount import Bank_account


my_account = Bank_account()


while True:

    print("""Choose the action you want to do with your bank account:
          1 - show the number of money in bank account
          2 - add money to bank account
          3 - get money from bank account
          4 - end the operation in the bank""")
    choose = int(input("Choose your action: "))
    if choose == 1:
        print(my_account)
    elif choose == 2:
        my_account.add_money_to_bank()
    elif choose == 3:
        my_account.get_money_from_bank()
    elif choose == 4:
        break
    else:
        break
