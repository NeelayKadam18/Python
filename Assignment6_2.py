
print("Application to demonstrate object oriented programming.\n")

class BankAccount:

    ROI = 10.5

    def __init__(self):
        self.Name = ""
        self.Amount = 0

    def Accept(self):
        print("Enter name : ")
        self.Name = input()
        print("Enter amount : ")
        self.Amount = int(input())

    def DisplayAccountInfo(self):

        print("------------Your Account Information is as follows--------------------")
        print("Name : ",self.Name)
        print("Initial Amount : ",self.Amount)

    def Deposit(self,value):
        self.Amount = self.Amount + value

    def Withdraw(self,value):
        self.Amount = self.Amount - value
        
def main():
    print("---------------------Banking Application------------------------")

    user1 = BankAccount()
    user2 = BankAccount()

    print("\nCreating the first account")
    user1.Accept()
    print("\nCreating the second account")
    user2.Accept()

    user1.DisplayAccountInfo()
    user2.DisplayAccountInfo()

    print("\n----------------------Withdrawal process for user 1 and 2--------------------------------")
    print("\nEnter amount to withdraw for user 1: ")
    value = int(input())
    user1.Withdraw(value)

    print("Amount of {} after withdraw is {} ".format(user1.Name, user1.Amount))

    print("\nEnter amount to withdraw for user 2: ")
    value = int(input())
    user2.Withdraw(value)

    print("Amount of {} after withdraw is {} ".format(user2.Name,user2.Amount))

    print("\n---------------------Deposit process for user 1 and 2-------------------------------------")
    print("\nEnter amount to deposit for user 1: ")
    value = int(input())
    user1.Deposit(value)

    print("Amount of {} after deposit is {} ".format(user1.Name, user1.Amount))

    print("\nEnter amount to deposit for user 2: ")
    value = int(input())
    user2.Deposit(value)

    print("Amount of {} after deposit is {} ".format(user2.Name,user2.Amount))

if __name__ == "__main__":
    main()