
print("Application to display pattern for a given number as input.")

def Pattern(no1):
    for i in range(no1):
        for j in range(no1):
            print(j+1, end="\t")
        print()
        
def main():
    print("Enter a number: ")
    no1= int(input())

    Pattern(no1)
        
if __name__ == "__main__":
    main()