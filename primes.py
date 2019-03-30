#Program to verify whether the input number is prime or not
#Prime number is divisable by itself and 1 only

#Get the input value from the user
n = int(input("Please enter a positive number: "))

#Prime numbers are greater than one so verify it
if n > 1:
    #Check and any other divisor
    for i in range(2, n):
        if(n % i == 0):
            print(int(n), "is not a Prime Number")
            print(i, "times", int(n/i), "is", n)
            break
    else:
        print(int(n), "is a Prime Number")
#If input value is less than 0 or equal to 1 then it is not a Prime number
else:
    print(n,"is not a Prime Number")

