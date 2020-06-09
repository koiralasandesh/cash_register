from store import *

sales = []
invoice = []

def main():
    while True:
        transaction()
        function = input("Press 0 for other function: ")
        if function == 0:
            sec_function()


def transaction():
    while True:    
        code = input ("Enter item code: ")
        for x in inventory:
            if code == x.code:
                invoice.append(x)        
        print("current invoice items: ")
        for x in invoice:
            x.display()
        print("\n")
        y = input ("press 0 to end transaction: ")
        if y==0:
            break
    return     

def sec_function():
    print("Secondary function not created yet!")
    add_item()

add_item()
print_inventory()
main()