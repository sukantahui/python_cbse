import os

project = "SBJW"
print("The platform is: ", os.name)
print("Welcome to ", project)
while True:
    print("Main Menu")
    print("1. book")
    print("2. Member")
    print("3. Transaction")
    print("4. Report")
    print("5. Exit")

    ch1 = int(input("Enter your Choice in Main Menu: "))
    if ch1<1 or ch1>5:
        print("Wrong choice ...............")
    if ch1 == 5:
        break
    if ch1 == 1:
        # Book area
        while True:
            print("\tBook Menu")
            print("\t1. Add")
            print("\t2. Update")
            print("\t3. Delete")
            print("\t4. Display")
            print("\t5. Exit")
            chBook = int(input("\tEnter your Choice in Book Menu: "))
            if chBook < 1 or chBook > 5:
                print("\tWrong choice in book menu ...............")
            if chBook == 5:
                break
