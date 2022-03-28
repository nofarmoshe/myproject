n1= int(input("enter n1: "))
n2= int(input("enter n2: "))
while n1%2==0 and n2%2==0:
    print(n1+n2)
    n1 = int(input("enter n1: "))
    n2 = int(input("enter n2: "))
if n1 % 2 > 0 or n2 % 2 > 0:
    print(n1 * n2)
