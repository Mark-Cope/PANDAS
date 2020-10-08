import pandas as pd

grades = pd.Series([87,100,94])

#print(grades)

myarray= pd.Series(98.6, range(3))

#print(myarray)

#print(grades[0])

#print(grades.describe()) #gives us all the stats

grades = pd.Series([87,100,94], index=['Wallie', 'Eva','Sam']) #how we assign names to things



grades = pd.Series({'Wally':87, 'Eva':100,'Sam':94}) #how to do it with a dictionary
'''
print(grades)

print(grades['Eva']) #How to get a spesific grade

print(grades.Eva) #same as above just with a . function

print(grades[1]) #same as above again just different way
'''


hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

a = hardware.str.contains('a') #pulls anything that has an 'a' in it

#print(a)

b= hardware.str.upper()

#print(b)

