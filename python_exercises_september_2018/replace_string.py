# Write a program to accept a string from user and replace not-bad with good
# Developed by : Chaitanya Deshpande
# Date : 29-08-2018
# Script Name : replace_string.py

# Program Begins

# Enter User Input a string which needs to be replaced For Eg : Sindhu played not that bad but still she lost

user_string = input("Enter the string from the User : ")
str(user_string)

# Enter the String which needs to be replace For Eg : not that bad

old_string = input("Enter the string which you wanted to replace : ")
str(old_string)

# Enter the String which you want after replacing for Eg : good

new_string = input("Enter the new string : ")
str(new_string)

# Replace Function is using

new_string1 = user_string.replace(old_string,new_string)

#Printing the New String

print(new_string1)

# Program Ends..

