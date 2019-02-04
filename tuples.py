# suppose a csv has the following data set

csvLine = '32,120000,10'

# define a tuple (immutable array/list) with '()' syntax and deconstruct the csv string into 3 variables
(age,income, yearsOfExperience) = csvLine.split(',')

personOne = (age,income, yearsOfExperience)
print(personOne)
