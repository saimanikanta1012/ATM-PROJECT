#ATMexemptions.py
class DepositError(Exception):
    def __init__(self,message="Dont enter Amount below Zero or Equal to Zero"):
        super().__init__(message)

class WithdrawError(Exception):
    def __init__(self,message="Dont enter Amount below Zero or Equal to Zero"):
        super().__init__(message)

class InsuffFundError(Exception):
    def __init__(self,message="Dont enter Amount below Zero or Equal to Zero"):
        super().__init__(message)
