from register import *

def main():
    print("===============Register Started========================")
    while True:
        print("1:\t\t Add inventory")
        print("2:\t\t Perform Transaction")
        print("3:\t\t Sales Report")
        print("4:\t\t Print Inventory")
        print("5:\t\t Shutdown Register")
        print("-------------------------------------------------------") 
        choice = input("Enter corresponding function number: ")
        if(int(choice) == 1):
            add_item()
        elif (int(choice) == 2):
            transaction()
        elif(int(choice) == 3):
            sales_report()
        elif(int(choice) == 4):
            print_inventory()
        elif(int(choice)==5):
            print("Shutting Down Register!")
            exit(0)
        else:
            print("Unknown input!")


main()