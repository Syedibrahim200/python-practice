class Product:
    def __init__ (self,t,a,q):
        self.title=t
        self.amount=a
        self.quantity=q
    def display(self):
        print()
        print("Displaying products\n--------------------")
        print("Title: ",self.title)
        print("Amount: ",self.amount)
        print("Quantity: ",self.quantity)
title = input("Enter product name: ")
product1 =Product(title,50000,50)
product1.display()