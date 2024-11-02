import random
randomnumber=random.randrange(1,200)
#print(randomnumber)
userinput=int(input("guess the number:"))
if userinput > randomnumber :
    print(randomnumber)
    print("the number is to high")
elif randomnumber> userinput:
    print(randomnumber)
    print("the number is too low")

else:
    print(randomnumber)
    print("matched the number")