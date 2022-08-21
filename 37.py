from random import randint
 
rand = randint(1, 100)
counter = 0
 
while True:
    counter+=1
    num=int(input("Enter values between 1 and 100 (0 exit):"))
    if(num==0):
        print("You canceled the game.")
        break
    elif num < rand:
        print("Enter a Higher Number.")
        continue
    elif num > rand:
        print("Enter a Lower Number.")
        continue
    else:
        print("Randomly selected number {0}!".format(rand))
        print("Your guess number {0}".format(counter))