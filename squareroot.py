#Program to print Square Root of the given number
#Import math module to use square root method
import math

#Get input from the user
n = float(input("Please enter a positive number: "))

sq_root = math.sqrt(n)
sq_root = format(sq_root, '.2f')
print ("The square root of", n, "is approx. ", sq_root )

