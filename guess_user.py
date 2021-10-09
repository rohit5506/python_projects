import random

def guess(x):
    random_num=random.randint(1,x)
    guess=0
    while guess != random_num:
        guess=int(input(f"guess a no. between 1 and {x} :"))
        if guess< random_num:
            print("sorry guess again,no. is too low")
        elif guess > random_num:
            print("sorry guess again,no is too high")
    print(f"yes you guessed it right : {random_num}")

guess(10)