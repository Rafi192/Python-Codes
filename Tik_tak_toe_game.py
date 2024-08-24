# This is a simple tiktak toe game implementation in python

def displayBoard(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


#displayBoard(row1,row2,row3)

def insertUserInput():
    options =['x','o']
    indices = [0,1,2]
    while True:
        userInput = input("Enter value either x or o :")
        if userInput not in options:
            print("invalid input! please enter 'x' or 'o'")
            continue

        indexInput = int(input("Enter index value between 0-2"))
        if indexInput not in indices:
            print("Invalid index! Enter index value between 0-2")
            continue
        return userInput,indexInput

def placeUserInput(row1,row2,row3):
    rows = [row1,row2,row3]
    
    while True:
        displayBoard(row1,row2,row3)
        rowChoice = int(input("Chose the row (0,1, or 2):"))
        if rowChoice not in [0,1,2]:
            print("Invalid row choice! please select 0,1,or 2")
            continue

        userInput , index = insertUserInput()
        if rows[rowChoice][index] == '':
            rows[rowChoice][index] = userInput
        else:
            print("THis position is already taken, chose another one")
            continue

        displayBoard(row1,row2,row3)


row1 = ['','','']
row2 = ['','','']
row3 = ['','','']
placeUserInput(row1,row2,row3)





