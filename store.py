from store_item import *

inventory = []

def add_item():
    while True:
        code = input("Enter/Scan code: ")
        name = input("Enter Name: ")
        desc = input("Enter Description: ")
        price = input("Enter Price: ")
        inv = input("Enter quantity: ")
        print("\n")

        temp_item = item (code,name,desc,price,inv)
        inventory.append(temp_item)
        check = input("Do you want to input more items? 1=yes/0=no : ")
        if int(check) == 0:
            print("\nAll items added! Auto Printing current Inventory!")
            print("-------------------------------------------------------")
            print_inventory()
            break


def print_inventory():
    for x in inventory:
        x.display()
        print("-------------------------------------------------------")


