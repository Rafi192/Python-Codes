# Using conventional method
def square(num):
    return num**2

myList = [1,2,3,4,5]
for i in myList:
    print(square(i))


# using python map function
print("Values using map\n")
#for item in map(square,myList):
#    print(item)
print(list(map(square,myList)))

# function to check if it contains even or odd number of words

def checkString(mystring):
    if len(mystring) %2 ==0:
        return "EVEN"
    else:
        return mystring[0]
senseiList = ["Uzawa", "Jubayer",'Roy','Sayourii']
print(list(map(checkString, senseiList)))
