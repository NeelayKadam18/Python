
print("Application to demonstrate object oriented programming.\n")

class BookStore:

    NoOfBooks = 0

    def __init__(self):
        self.Name = ""
        self.Author = ""
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Accept(self):

        print("Enter Name of Book: ")
        self.Name = input()

        print("Enter Name of Author: ")
        self.Author = input()

    def Display(self):
        print("\n{} by {}. No of Books : {}.\n".format(self.Name,self.Author,BookStore.NoOfBooks))

def main():
    obj1 = BookStore()
    obj1.Accept()
    obj1.Display()
    obj2 = BookStore()
    obj2.Accept()
    obj2.Display()

if __name__ == "__main__":
    main()