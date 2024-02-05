from bankaccount2 import BankAccount, MinimumBalanceAccount


# account = BankAccount()

# account.deposit(500)

# amountToWithdraw = 300

# result = account.try_withdraw(amountToWithdraw)

# if result.isSuccess:
#     print(result.message)

accountMin = MinimumBalanceAccount(1500, 1000)

result = accountMin.try_withdraw(400)

if result.is_ok():
    print(result.message)
