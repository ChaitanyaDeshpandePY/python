# Write a Python Program to accept a string from the User, replace the occurrence of first character ( any which you selects ) in remaining part of string with *
# Example : Here we take example as a - chaitanya, for other strings please change the below positions in print(m[2]) and m.replace (a) and print(m[:3] + y[3:])
# Developed by : Chaitanya Deshpande
# Date : 28-08-2018
# Script Name : star_replace_in_string.py

# Program Begins

# Enter the User Input

m = input("Enter the string : ")
str(m)
print(m[2])

 

# Replacing  the first character - a with *
y = m.replace('a','*',)
print(y)

# Printing the Complete string
print(m[:3] + y[3:])

# Program Ends..

 

