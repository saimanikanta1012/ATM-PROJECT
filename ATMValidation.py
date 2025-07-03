#ATMValidation.py
from USERinfo import Users
def AccHoldNames():
    while(True):
        try:
            user_data=Users()
            name=str(input("Enter the Account Holder Name:").upper())
            if name in user_data:
                while(True):
                    try:
                        pin=int(input("Enter the 4-DIGIT PIN:"))
                        if pin==user_data [name]['pin']:
                            print("="*50)
                            print("\t\tLogin Successful")
                            print("=" * 50)
                            return name
                        else:
                            print("-" * 50)
                            print("\t\tIncorrect Credintials")
                            print("-" * 50)
                    except ValueError:
                        print("Don't Enter Alphabets,Symbols--- Enter only Four DIGIT PIN")
            else:
                print("Invalid Account Holder Name")
        except ValueError:
            print("Enter a Valid Account Holder Name.")