numbers = [11, 22, 35, 40, 53, 64, 77, 80]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
     
print("Original list =",numbers)
print("Even numbers are =",even_numbers)

