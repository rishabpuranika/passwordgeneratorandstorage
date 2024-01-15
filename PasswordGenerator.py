import random               #importing random module
from PasswordGeneratorFunctions import *    #importing all the functions from passwordgeneratorfunctions.py


#main program
print('*'*30)
print("Welcome to the password generator")
print('*'*30)
main1()
f = input("Do you want to continue? (Enter y or n): ")
if f.lower() == "y":
    main1()
else:
    exit()
