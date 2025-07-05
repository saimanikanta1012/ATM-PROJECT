# 🏦 ATM Project in Python

This is a console-based ATM Simulation built with Python.  
It simulates core banking operations like deposit, withdrawal, and balance inquiry, 
along with PIN-based user login and custom error handling.

---

## 🚀 Features

- 🔐 PIN-based secure user login
- 💰 Deposit and Withdraw operations
- 📋 Balance Enquiry
- ❌ Custom Exceptions (Negative amounts, Insufficient funds)
- 🧱 Modular Python code (each function in its own file)

---

## 📁 File Descriptions

| File Name                           | Description                                                                   |
|----------------------------------------|-----------------------------------------------------------------------------|
| `ATMOperationsDemo.py`  | ✅ Main driver script (Run this to start the program) |
| `ATMmenu.py`                    | Displays menu options for operations                        |
| `ATMValidation.py`             | Handles user login and PIN validation                        |
| `BankOperations.py`          | Handles deposit, withdraw, and balance logic            |
| `USERinfo.py`                     | Contains sample account holders and PINs               |
| `ATMexemptions.py`          | Defines custom exceptions for input validation         |
----------------------------------------------------------------------------------------------------------------------
---

## 🧪 Sample Users for Testing

Use the following details when prompted during login:

| Name        | PIN    | Balance |
|----------------| ---------|-------------|
| USER1      | 1234  | ₹1967    |
| USER2      | 3456  | ₹1540    |
| USER3      | 5678  | ₹6200    |
| USER4      | 7890  | ₹3450    |

✅ These users are loaded from `accounts.pkl`.  
If the file is missing, it will be auto-generated using `USERinfo.py`.

---

## 💾 Data Storage

- The ATM system uses a file called `accounts.pkl` to store user balances and PINs persistently.
- The file is read at the start and updated after every transaction.
- If `accounts.pkl` does not exist, the system loads default users from `USERinfo.py` and creates the file automatically.

---
## 🏁 How to Run

1. Make sure you have Python installed (version 3.x).
2. Place all `.py` files in the same folder.
3. Open a terminal in that folder.
4. Run the following command:

```bash
python ATMOperationsDemo.py

5.Login using any of the test names and PINs above.
6.Choose operations from the displayed menu.

Project Folder Structure

ATM-Project/
├── ATMOperationsDemo.py      # Main program file
├── ATMmenu.py                        # Menu display logic
├── ATMValidation.py                 # User login validation
├── BankOperations.py              # Core banking operations
├── USERinfo.py                        # Sample user data
├── ATMexemptions.py             # Custom exceptions
└── README.md                       # Documentation

🙋‍♂️ Author
Project by **Sai Manikanta Tippana** — Aspiring Python Full Stack Developer  
📧 saitippana102002@gmail.com | 🔗 LinkedIn: linkedin.com/in/saimanikanta-tippana


⭐ Star this repo if you found it useful!
💬 Feel free to raise issues or suggestions!
