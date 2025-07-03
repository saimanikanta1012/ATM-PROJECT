#BankOperations.py<---File name and Module name
from ATMexemptions import DepositError,WithdrawError,InsuffFundError
from USERinfo import Users
Bal_data=Users()
def deposit(name):
    damnt=float(input("Enter the Amount to Deposit:")) #chance of getting error
                                                       # like value error and less than zero error
    if (damnt<=0):
        raise DepositError
    else:
        Bal_data[name]['balance']+=damnt
        print("-" * 50)
        print("Your Account XXXXXX4567 Credited with INR {}".format(damnt))
        print("-" * 50)
        print("Now Your Available Balance is INR {}".format(Bal_data[name]['balance']))
        print("-" * 50)
    return Bal_data[name]['balance']
def Withdraw(name):
    wamnt= float(input("Enter the Amount to be WithDrawn:"))#chance of getting error
    if (wamnt<=0):
        raise WithdrawError
    elif(wamnt>Bal_data[name]['balance']):
        raise InsuffFundError
    else:
        Bal_data[name]['balance']=Bal_data[name]['balance']-wamnt
        print("-" * 50)
        print("Your Account XXXXXXX4567 Debited with INR {}".format(wamnt))
        print("-" * 50)
        print("Now Your Available Balance is INR{}".format(Bal_data[name]['balance']))
        print("-" * 50)
def BalEnquiry(name):
    print("-" * 50)
    print("Your Available Balance is INR {}".format(Bal_data[name]['balance']))
    print("-" * 50)
