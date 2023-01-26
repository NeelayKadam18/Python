# Instance varible : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()

class Bank_Account:

    def __init__(self):
        self.Name = ""
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

def main():
    user1 = Bank_Account()
    user2 = Bank_Account()

    print("\nCreating the first account")
    user1.CreateAccount()
    print("\nCreating the second account")
    user2.CreateAccount()

    user1.DisplayAccountInfo()
    user2.DisplayAccountInfo()
    
if __name__ == "__main__":
    main()