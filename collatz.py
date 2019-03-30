#Program to output successive values of user defined calculation
#If I/P value is even then divid it by 2 or if it is odd then mutiply by 3 and add one.
#Continue to print until value is one

n = int(input("Please enter a positive integer: "))

if n > 0:
    #print out put
    print(n, end = " " )
    while n > 1:
        if (n % 2 == 0):
            n = n/ 2
            print(int(n), end = " " )
        else:
            n = (n * 3) + 1
            print(int(n), end = " " )
else:
    print ("Oops, It is a negative number") 