from store_item import item

inventory = []

def add_item():
    while True:
        code = input("Enter code for the item: ")
        name = input("Enter Name: ")
        desc = input("Enter Description: ")
        price = input("Enter Price: ")
        inv = input("Enter quantity:")
        print("\n")

        temp_item = item (code,name,desc,price,inv)
        inventory.append(temp_item)
        check = input("Do you want to input more items? 1=yes/0=no : ")
        if int(check) == 0:
            print("All items added!\n")
            break

def print_inventory():
    print("Printing inventory:")
    for x in inventory:
        x.display()

add_item()
print_inventory()