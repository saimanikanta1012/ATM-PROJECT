#ATMOperationsDemo.py
from ATMmenu import menu
from BankOperations import deposit,Withdraw,BalEnquiry
from ATMValidation import AccHoldNames, save_accounts
from ATMexemptions import DepositError,WithdrawError,InsuffFundError
name,accounts =AccHoldNames()
while(True):
    menu()
    try:
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                try:
                    deposit(name,accounts)
                    save_accounts(accounts)
                except DepositError:
                    print("\tDon't try to Deposit -VE / Zero Amount")
            case 2:
                try:
                    Withdraw(name,accounts)
                    save_accounts(accounts)
                except WithdrawError:
                    print("\tDon't try to Deposit -VE / Zero Amount")
                except InsuffFundError:
                    print("Insufficient Funds in your Accounts")
            case 3:
                BalEnquiry(name,accounts)
            case 4:
                print("=" * 50)
                print("Thanks for Using this ATM.")
                print("=" * 50)
                break
            case _:
                print("Your Selection of Operation is Invalid---Try Again")

    except ValueError:
        print("Don't enter alphabets, symbols---Try Again")

