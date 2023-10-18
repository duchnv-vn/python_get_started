# print('===== CLASS START =====')

# class Account:
#   def __init__(self,account_number,account_type, initial_balance):
#     self.account_number = account_number
#     self.account_type = account_type
#     self.balance = initial_balance

#   def deposit(self, amount):
#     if amount > 0:
#       self.balance += amount
#       print(f'Deposited {amount}')
#       print(f'New balance is {self.balance}')
#     else:
#       print(f'{amount} is an invalid amount')

#   def withdraw(self, amount):
#     if amount > 0 and amount <= self.balance:
#         self.balance -= amount
#         print(f'Withdrawal {amount}')
#         print(f'New balance is {self.balance}')
#     else:
#       if amount <= 0:
#         print(f'{amount} is an invalid amount')
#       else:
#         print(f'Current balance {self.balance} is not enough')


# my_account = Account('123-456', 'savings', 1_000_000.00)

# my_account.withdraw(500_000)
# my_account.withdraw(500_000)
# my_account.withdraw(500_000)

# print('===== CLASS END =====')

print('===== VARIABLE START =====')
budget = 3000

car = 'TOYOTA' if budget > 2000 else 'VINFAST'

print(car)

print('===== VARIABLE END =====')