data=input("Enter a word to check: ")
check=""
for x in data:
    check=x+check
if(data==check):
    print("String is palindrome")
else:
    print("String is not palindrome")