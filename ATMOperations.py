#ATMOperations.py<---Module Name
from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.0 #Global Var
def deposit():
    damt=float(input("Enter Ur Deposit Amount:")) # Implcitly PVM may raise ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUR Account xxxxxxxx123 Credited with INR:{}".format(damt))
        print("\tUR Account xxxxxxxx123 Bal after Deposit INR:{}".format(bal))

def withdraw():
    global bal
    wamt = float(input("Enter Ur Withdraw Amount:"))  # Implcitly PVM may raise ValueError
    if(wamt<=0):
        raise WithDrawError
    elif(wamt+500)>bal :
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("\tUR Account xxxxxxxx123 Debited with INR:{}".format(wamt))
        print("\tUR Account xxxxxxxx123 Bal after Withdraw INR:{}".format(bal))

def balenq():
    print("\tUR Account xxxxxxxx123 Bal INR:{}".format(bal))

