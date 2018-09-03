# Write a Program to accept a string from user and print it in a reverse way
# Developed by : Chaitanya Deshpande
# Date : 28-08-2018
# Script Name : reverse.py

# Program Begins

# Accepting the User Input

user_string = input("Enter a string which is to be reversed : ")
str(user_string)

# Implementing the Reversal

y = user_string[::-1]

# Printing the Reversal of String

print("Reversal of String :" + " " + str(user_string) + " " + "is" + " " + str(y))
# Program Ends


