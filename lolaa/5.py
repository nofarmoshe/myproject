n1=int(input("Enter a number:"))
while 10<=n1<=99:
    if n1%10==7 or n1//10%10==7 or n1%7==0:
        print("lucky number")
    n1 = int(input("Enter a number:"))



