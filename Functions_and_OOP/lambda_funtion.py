# a labda expression is a typical funtion without the def keyword and the function name
# for example
lamdaVar=lambda num: num**2
print(lamdaVar(5))
#output -> 25

#2. Lambda function with map()
myNum = [1,2,3,4,5,6]
print(list(map(lamdaVar,myNum)))

#output -> [1, 4, 9, 16, 25, 36]

#3. Lambda with filter() function
Even = lambda numList: numList%2==0
print(list(filter(Even,myNum)))

#output -> [2, 4, 6]

#4. lambda with string and map()
senseiList = ["Uzawa", "Jubayer",'Roy','Sayourii']
print(list(map(lambda x: x[::-1],senseiList)))
