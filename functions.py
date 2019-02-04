def SquareIt(number): 
	return number * number

def FunctionAsParameter(function, number):
	# this function accepts another function as its first argument
	return function(number)

# print(FunctionAsParameter(SquareIt, 5))

# lambda/annonymous function. here the lambda takes 1 argument, num. 
print FunctionAsParameter(lambda num: num*num*num, 3)
