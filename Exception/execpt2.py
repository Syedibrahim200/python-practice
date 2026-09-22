print("This program is to find area".upper())
try:
    x = int(input("Enter lenght: "))
    y = int(input("Enter breadth: "))
    area = x*y
except ValueError:
    print("Please enter whole numbers only")
except ZeroDivisionError:
    print("Second number should not be zero(0)")
else: 
    print("Area =", area)
