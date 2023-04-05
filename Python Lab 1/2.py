
def valid():
    number= int(input("Enter a Number : "))
    if(number==0):
        print("Zero is Neither Even or Odd")
    else:
        if(number%2==0):
            print("Entered Number is Even")
        else:
            print("Entered Number is Odd")
    exit=input("continue (y/n): ")
    while True:
        if (exit=="y"):
            valid()
        else:
            print("Program Terminated")
        break;
result=valid()