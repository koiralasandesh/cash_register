class item:
    code = "N/A"
    name = "N/A"
    desc = "N/A"
    price = 0.00
    inventory = 0

    def __init__ (self,c, n, d, p,i):
        self.code=c
        self.name = n
        self.desc = d
        self.price = p
        self.inventory = i
    
    def display(self):
        print ("Item Name: \t\t"+ self.name)
        print("Item Code: \t\t"+ self.code)
        print("Item Description: \n" + self.desc)
        print("Item Price: \t\t"+ str(self.price))
        print ("Item Inventory: \t\t"+str((self.inventory))
        



