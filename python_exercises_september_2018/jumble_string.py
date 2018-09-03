# Write a Program to accept 2 strings from the User and jumble them ( swap the first 2 characters of both and prints the string )
# Developed by : Chaitanya Deshpande
# Date : 28-08-2018
# Script Name : jumble_string.py

# Program Begins

# Accepting the User Inputs

user_string1 = input("Enter first string : ")
str(user_string1)
user_string2 = input("Enter second string : ")
str(user_string2)
print(user_string1)
print(user_string2)

# Jumbling the user inputs

print(user_string1[:2] + user_string2[2:])
print(user_string2[:2] + user_string1[2:])

# Program Ends..

