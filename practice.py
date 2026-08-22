numbers = [45, 12, 78, 34, 91, 23, 67]
largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    
    if number > largest:
     largest = number
    if number < smallest:
     smallest = number
print("Largest: ",largest) 
print("smallest: ",smallest) 
     