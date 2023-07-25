import random

def GuessRand(num):
    random_number=random.randint(1,num)
    Guess=0
    while Guess !=random_number:
        Guess=int(input(f'Enter a number betweeen 1 to {num}'))
        if Guess==random_number:
            print(f"Gueseeed the right number {random_number}")
        elif Guess>random_number:
            print("Sorry, Too high nummber, Try again")
        elif Guess<random_number:
            print("Sorry, Too Low number, Try again.")

GuessRand(10)


