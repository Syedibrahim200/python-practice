class Car:
    def __init__ (self,brand,year,price):
        self.brand=brand
        self.year=year
        self.price=price
    def display(self):
        print()
        print("Displaying your car details\n--------------------")
        print("Brand: ",self.brand)
        print("Year: ",self.year)
        print("Price: ",self.price)
title = input("Enter Car name:")
# print(" and\nif you get the car name correct\nyou will have a suprice car".upper())

car1=Car(title,2020,"500M") 
if title == "Toyota":
    print("Price of Toyota is only 25lakhs")
else:
    car1.display()