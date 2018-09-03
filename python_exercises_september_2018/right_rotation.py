# Write a program to check if second string is right rotation of first (assume their lengths are same)
# Developed by : Chaitanya Deshpande
# Date : 29-08-2018
# Script Name : right_rotation.py

# Program Begins

# Entering the String 1 and String 2 as Inputs : Eg. string 1 = "manager" and string = "germana"

x = input("Enter string 1 : ")
str(x)
y = input("Enter string 2 : ")
str(y)

#Rotating the Second String to Right

z=y[3:] + y[:3]

# Checking whether After Rotation of Second String it matches with First or now
print(x==z)

# Accepting the third string : Eg. String 3 = manrage

z1 = input("Enter string 3 : ")

z2 = z1[3:] + z1[:3]

# Comparing the original and changed strings
print(x==z2)

# Program Ends

