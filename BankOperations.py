#BankOperations.py<---File name and Module name
from ATMexemptions import DepositError,WithdrawError,InsuffFundError

def deposit(name,accounts):
    damnt=float(input("Enter the Amount to Deposit:")) #chance of getting error
                                                       # like value error and less than zero error
    if (damnt<=0):
        raise DepositError
    else:
        accounts[name]['balance']+=damnt
        print("-" * 50)
        print("Your Account XXXXXX4567 Credited with INR {}".format(damnt))
        print("-" * 50)
        print("Now Your Available Balance is INR {}".format(accounts[name]['balance']))
        print("-" * 50)
    return accounts[name]['balance']
def Withdraw(name,accounts):
    wamnt= float(input("Enter the Amount to be WithDrawn:"))#chance of getting error
    if (wamnt<=0):
        raise WithdrawError
    elif(wamnt>accounts[name]['balance']):
        raise InsuffFundError
    else:
        accounts[name]['balance']=accounts[name]['balance']-wamnt
        print("-" * 50)
        print("Your Account XXXXXXX4567 Debited with INR {}".format(wamnt))
        print("-" * 50)
        print("Now Your Available Balance is INR{}".format(accounts[name]['balance']))
        print("-" * 50)
def BalEnquiry(name,accounts):
    print("-" * 50)
    print("Your Available Balance is INR {}".format(accounts[name]['balance']))
    print("-" * 50)
