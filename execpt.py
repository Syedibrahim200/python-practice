print("This program is to multiply two numbers".upper())
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    multi = x*y
except ValueError:
    print("Please enter whole numbers only")
except ZeroDivisionError:
    print("Second number should not be zero(0)")
else: 
    print("Result =", multi)
