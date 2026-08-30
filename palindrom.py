name = input("Enter a word: ")
reverse = name[::-1]
if name == reverse:
    print("The word you entered is a"" palindrom".upper())
else:
    print("The word you entered is not a palindrom".upper())