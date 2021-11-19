import random
random_no = random.randint(1, 10)

print("Random Number:", random_no)
guess = int(input("Enter an integer from 1 to 10: "))


if random_no == guess:
    print("Equal")
elif abs(random_no - guess) == 1:
    print("close to random number")
else:
    print ("TOO far from random number")

