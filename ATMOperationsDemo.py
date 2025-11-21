#ATMOperationsDemo.py<--Main Program
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
from ATMExcept import DepositError,WithDrawError,InSuffFundError
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDON'T ENTER -VE OR ZERO FOR DEPOSIT AMOUNT")
                except ValueError:
                    print("\tDON'T ENTER ALNUMS / STRS / SPECIAL SYMBOLS FOR DEPOSIT AMOUNT")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDON'T ENTER -VE OR ZERO FOR WITHDRAW AMOUNT")
                except InSuffFundError:
                    print("\tUR ACCOUNT DOES NOT CONTAIN SUFF. FUNDS-READ PYTHON NOTES")
                except ValueError:
                    print("\tDON'T ENTER ALNUMS / STRS / SPECIAL SYMBOLS FOR WITHDRAW AMOUNT")
            case 3:
                balenq()
            case 4:
                print("Thx for using this project")
                break
            case _:
                print("\tUr Selection of Operation is wrong-try again")
    except ValueError:
        print("\tDon't enter alnums/strs/symbols for IntegerChoice-try again")
