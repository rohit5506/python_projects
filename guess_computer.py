import random

def guess_comp(x):
    low=1
    high=x
    feedback=""
    while feedback!= "c":
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'if {guess} is too high :H , is too low:L,is correct: C ').lower()
        if feedback=="h":
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"congrates computer guessed your no. ,{guess},correctly")

guess_comp(10)