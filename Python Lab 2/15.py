import random
import string
length=int(input("Enter the length of the password: "))
all=string.ascii_letters+string.digits+string.punctuation
temp=random.sample(all,length)
password="".join(temp)
print(password)