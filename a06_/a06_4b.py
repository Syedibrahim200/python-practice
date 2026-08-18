numbers = [45, 12, 78, 34, 91, 23, 67]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("The largest number =",largest)
print("The smallest number =",smallest)