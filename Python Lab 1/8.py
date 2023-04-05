import random
def guess():
    guessnum=random.randrange(1,10)
    number= int(input("Guess a number: "))
    if number<guessnum:
        print("Guessed number is low")
    if number>guessnum:
        print("Guessed number is High")
    if number==guessnum:
        print("Guessed number is exactly right") 
    exit=input("enter y to continue: ")
    while True:
        if(exit=='y'):
            guess()
        else:
            print("game Terminated!")
            break;
run=guess()
