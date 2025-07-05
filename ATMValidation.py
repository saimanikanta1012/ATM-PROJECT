#ATMValidation.py
import os
from USERinfo import Users
import pickle

def load_accounts():
    if os.path.exists("accounts.pkl"):
        with open("Accounts.pkl","rb") as f:
            return pickle.load(f)
    else:
        print("⚠️ accounts.pkl not found. Loading from USERinfo.py")
        data = Users()  # Load sample users from USERinfo.py
        with open("accounts.pkl", "wb") as f:
            pickle.dump(data, f)
        print("✅ accounts.pkl created successfully from USERinfo.py")
        return data
def save_accounts(data):
    with open("Accounts.pkl","wb")as f:
        return pickle.dump(data,f)

def AccHoldNames():
    while(True):
        try:
            accounts=load_accounts()
            name=input("Enter the Account Holder Name:").upper()
            if name in accounts:
                while(True):
                    try:
                        pin=int(input("Enter the 4-DIGIT PIN:"))
                        if pin==accounts [name]['pin']:
                            print("="*50)
                            print("\t\tLogin Successful")
                            print("=" * 50)
                            return name,accounts
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
