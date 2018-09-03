# Write a Program to Accept a String from user and accept the start index, end index from the user and display the result of slicing
# Input - In this example we used string - chaitanya
# Devloped by : Chaitanya Deshpande
# Date : 28-08-2018
# Script Name : slicing_intro.py

#Program beginning

# Accepting User Input

user_string = input("Enter the String : ")

str(user_string)

print("\n")

#Accepting Start and End Index for Positive Integers

start_index = input("Enter the Start Index for Positive Integers: ")

int(start_index)

end_index = input("Enter the End Index for Positive Integers: ")

int(end_index)

#Accepting Start and End Index for Negative Integers

print("\n")

start_index1 = input("Enter the Start Index for Negative Integers: ")

int(start_index1)

end_index1 = input("Enter the End Index for Negative Intgers: ")

int(end_index1)

print("\n")

print("Slicing of the String : " + " " + str(user_string))

 

# Implementing the Slicing for Positive Integers

new = user_string[int(start_index):int(end_index)]

# Implementing the Slicing for Negative Integers

new1 = user_string[int(start_index1):int(end_index1):-1]

#Printing the result of Slicing

print("\n")

print("Printing the Result of Slicing for Positive Integers :")

print(str(new))

print("\n")

print("Printing the Result of Slicing for Negative Integers :")

print(str(new1))

# Program Ends

