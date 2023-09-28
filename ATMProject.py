import os
class Atm:
    def __init__(self):
        self.pin_number = ""
        self.Balance = 0
        self.Data = [1234, 4567, 8901, 3027, 2140, 8055, 3996]
        self.menu()
    def menu(self):
        User_input = int(input("________________ATM SERVICE_____________________ \n"
                               "            *** Enter Your Response ***" '\n'
                               " ---->    If You Want Withdraw Amount Plz Enter    : 1"'\n'
                               " ---->    If You Want Deposit Plz Enter            : 2"'\n'
                               " ---->    If You Want Check Your Balance Plz Enter : 3"'\n'
                               " ---->    If You Want Exit Plz Enter               : 4"'\n'
                               ))
        if User_input == 1:
            self.Withdraw()
        elif User_input == 2:
            self.Deposit()
        elif User_input == 3:
            self.Check()
        else:
            print("Exits Thank You !!!")
            os.environ['TERM'] = 'xterm-256color'
            os.system('clear')
    def Withdraw(self):
        temp = int(input("Enter Your Pin Number"))
        if temp in self.Data:
            amount = int(input("Plz Enter Your Amount :"))
            if amount <= self.Balance:
                self.Balance = self.Balance - amount
            else:
                print("Enter Your Account has Not Sufficient  Amount")
        else:
            print("Plz Enter Your Correct Pin number")
        self.menu()

    def Deposit(self):
        temp = int(input("Enter Your Pin Number : "))
        if temp in self.Data:
            amount = int(input("Plz Enter Your Amount :"))
            self.Balance = amount + self.Balance
            print("Succefully Deposit Your Amount")
        else:
            print("Plz Enter Valid Pin Number")
        self.menu()
    def Check(self):
        temp = int(input("Enter Your Pin Number"))
        if temp in self.Data:
            print("Your Balance is :", self.Balance)
        else:
            print("Enter a Valid Pin Number")
        self.menu()
SBI = Atm()
SBI
