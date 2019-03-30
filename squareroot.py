#Program to print Square Root of the given number
#Import math module to use square root method
import math

#Get input from the user
n = float(input("Please enter a positive number: "))

#Find Square root of the input value using math.sqrt method
sq_root = math.sqrt(n)

#If the output is float value then format it to 2 decimal place
if (sq_root.is_integer() == False):
    sq_root = format(sq_root, '.2f')
#if the output is not a float value then return a whole number 
else:
    sq_root = int(sq_root)
    n = int(n)

print ("The square root of", n, "is approx. ", sq_root )