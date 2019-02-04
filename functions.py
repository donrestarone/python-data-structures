def SquareIt(number): 
	return number * number

def FunctionAsParameter(function, number):
	# this function accepts another function as its first argument
	return function(number)

print(FunctionAsParameter(SquareIt, 5))

