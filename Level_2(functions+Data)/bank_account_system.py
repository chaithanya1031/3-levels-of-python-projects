account=[]
def deposit(money):
    account.append(money)
    print(f'{money} rupees deposited')
def withdraw(money):
    account[0]=account[0]-money
    print(f'{money} is withdrawn')
def check_balance():
    print(f'you have {account[0]} rupees in your account')
print('======Welcome to overseas bank======')
while True:
    print("****************************************")
    action=input('choose 1 to deposit\nchoose 2 to withdraw\nchoose 3 to check balance\nchoose 4 to exit:')
    if action=='1':
        deposit(int(input('enter deposit amount:')))
    elif action=='2':
        withdraw(int(input('enter withdraw amount:')))
    elif action=='3':
        check_balance()
    elif action=='4':
        break
    else:
        print('invalid input')