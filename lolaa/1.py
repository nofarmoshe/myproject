n= int(input("Enter a n:"))
while 100<=n<1000:
        t=n%10
        t1=n//10%10
        t2=n//100
        print(t+ t1+ t2)
        n = int(input("Enter a n:"))
print("invalid n")


