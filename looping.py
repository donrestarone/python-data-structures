from functions import SquareIt

listOfNumbers = range(100000000)

for x in listOfNumbers:
	if SquareIt(x) % 2 == 0:
		print('even!: ', x)	
	elif SquareIt(x) % 5 == 0:
		print('divisible by 5!: ', x)	
	else: 
		print('idont know:', x)