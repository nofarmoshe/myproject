import random
n= random.randint(1,9)
print(n)
guess=int(input("guess a number:"))
while guess>n or guess<n:
    if guess>n:
        print("big number")
    if guess<n:
        print("low number")
    guess = int(input("guess a number:"))
if guess==n:
    print("good")




