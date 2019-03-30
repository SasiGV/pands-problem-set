#Program to calculate sum of numbers from 1 to the number entered

#Get input from User
n=int(input("Enter an Integer Number to calculate Sum"))

#Create an empty intergar called Sum and set initialie it to zero
sum = 0

#Create a For look and add number starts from 1 upto the number entered
for num in range (0, n+1, 1):
    sum = sum + num 
#Print the output value    
print ("Sum of first ", n, "number is: ", sum)
