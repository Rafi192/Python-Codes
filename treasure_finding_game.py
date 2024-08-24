# Simple Treasure finding game ->
from random import shuffle
#shuffle list
def shuffle_list(myList):
    shuffle(myList)
    return myList

mylist= ['','','treasure']
#take player guess
def player_guess():
    guess =''
    while guess not in ['0','1','2','3']:
        guess = input("Pick an index number : 0, 1 ,or 2\n")

    return int(guess)

playerGuess = player_guess()
#check player guess
def check_guess(mylist, guess):
    if mylist[guess] == 'treasure':
        print("You found the Treasue!!\n")
    else:
        print("sorry, you didn't found the treasue :( !")
        print("The treasure was hidden at index",mylist.index('treasure'))

# Check result ( if treasure has been found by player or not)
check_guess(mylist, playerGuess)
