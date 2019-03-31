#Sasikala Varatharajan G00376470
#Program to output successive values of user defined calculation
#If input value is even then divide it by 2 or if it is odd then mutiply by 3 and add one.
#Continue to print until the value is becomes one

#Get input from user
n = int(input("Please enter a positive integer: "))

#Verify the input whether it is Positive or not
if n > 0:
    #Start to print out put
    #end = " " will print the next value with a space instead of a new line
    print(n, end = " " )
    #Start the loop and print the output unitl n becomes value 1
    while n > 1:
        #If n in even then divide it by 2
        if (n % 2 == 0):
            n = n/ 2
            print(int(n), end = " " )
        #if n is odd then multiply by 3 and add 1
        else:
            n = (n * 3) + 1
            print(int(n), end = " " )
else:
    print ("Oops, It is a negative number") 