#ATMOperationsDemo.py
from ATMmenu import menu
from BankOperations import deposit,Withdraw,BalEnquiry
from ATMValidation import AccHoldNames
from ATMexemptions import DepositError,WithdrawError,InsuffFundError
name=AccHoldNames()
while(True):
    menu()
    try:
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                try:
                    deposit(name)
                except DepositError:
                    print("\tDon't try to Deposit -VE / Zero Amount")
            case 2:
                try:
                    Withdraw(name)
                except WithdrawError:
                    print("\tDon't try to Deposit -VE / Zero Amount")
                except InsuffFundError:
                    print("Insufficient Funds in your Accounts")
            case 3:
                BalEnquiry(name)
            case 4:
                print("Thanks for Using this Program.")
                break
            case _:
                print("Your Selection of Operation is Invalid---Try Again")

    except ValueError:
        print("Don't enter alphabets, symbols---Try Again")

