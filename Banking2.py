# Instance varible : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()
# Class Varible : Bank_Name, ROI_On_FD
# Class method : DisplayBankInformation
# Static method : DisplayKYCInfo

class Bank_Account:

    Bank_Name = "HDFC bank PVT LTD"     # Class Variable
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name = ""                  # Instance Variable
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your initial amount : ")
        self.Amount = int(input())

        print("Enter your Address : ")
        self.Address = input()

        print("Enter your Account number : ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):

        print("------------Your Account Information is as follows--------------------")
        print("Name : ",self.Name)
        print("Account Number : ", self.AccountNo)
        print("Initial Amount : ",self.Amount)
        print("Address : ",self.Address)

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to Banking console")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of interest we offer on fixed deposit is : ",cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC information : ")
        print("According to the rules of Government of India, you have to submit following documents : ")
        print("1 : Clear and recent passport size photo.")
        print("2 : Photo of Aadhar Card.")
        print("3 : Photo of Pan Card.")

    def Deposit(self,value):
        self.Amount = self.Amount + value

    def Withdraw(self,value):
        self.Amount = self.Amount - value

def main():

    print("---------------------Banking Application------------------------\n")

    print("Static Method - KYC Info \n")
    Bank_Account.DisplayKYCInfo()

    print("---------------------Accessing class varibles from main----------------------\n")
    print("Name of Bank : ",Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed Deposit : ",Bank_Account.ROI_On_FD)

    print("---------------------Calling class method to display bank information----------------------\n")
    Bank_Account.DisplayBankInformation()
    
    user1 = Bank_Account()
    user2 = Bank_Account()

    print("\nCreating the first account")
    user1.CreateAccount()
    print("\nCreating the second account")
    user2.CreateAccount()

    print("---------------------Calling instance method to display information of first account----------------------\n")
    user1.DisplayAccountInfo()
    print("---------------------Calling instance method to display information of second account----------------------\n")
    user2.DisplayAccountInfo()

    print("----------------Deposit 200 in user1-------------------\n")
    user1.Deposit(200)
    print("Amount of {} after deposit is {} ".format(user1.Name, user1.Amount))
    print("----------------Deposit 500 in user2-------------------\n")
    user2.Deposit(500)
    print("Amount of {} after deposit is {} ".format(user2.Name,user2.Amount))

    print("----------------Withdraw 200 from user1-------------------\n")
    user1.Withdraw(200)
    print("Amount of {} after withdraw is {} ".format(user1.Name, user1.Amount))
    print("----------------Withdraw 100 from user2-------------------\n")
    user2.Withdraw(100)
    print("Amount of {} after withdraw is {} ".format(user2.Name,user2.Amount))

if __name__ == "__main__":
    main()