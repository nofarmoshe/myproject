import random
n= int(input("enter n between 0-100:"))
while 0>n or n>100:
    n = int(input("enter n between 0-100:"))
x=random.randint(0,100)
print (x)
while x>n or x<n:
    if x>n:

    if x<n:
        print("high")
    n = int(input("enter n between 0-100:"))
if x==n:
    print("good")
