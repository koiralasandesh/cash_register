from store import *
#from invoice import *

sales = []
invoice =[]
def transaction():
    while True:  
        print("-------------------------------------------------------")  
        code = input ("Enter/Scan code: ")
        for x in inventory:
            if code == x.code:
                invoice.append(x)        
                print("Item Added to invoice.\n")
        print("Current invoice items: ")
        print("------------------")
        for x in invoice:
            x.display()
            print("------------------")
        y = input ("press 0 to end transaction: ")
        if int(y)==0:
            sales.append(invoice)
            return

def sales_report():
    for x in sales:
        print("Printing Sales Report: ")
        print("------------------")
        for y in x:
            y.display()
            print("------------------")