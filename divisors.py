#Sasikala Varatharajan G00376470
#Program to find all divisors between the given two numbers

#In this program we are going to find the numbers divisble by 6 but not by 12

#Get two inputs from the user - As per the instructions it should use 1000 as int_From and 10000 as int_to.
#But I have given an option to the user to select the range
int_From = int(input("Enter the Range of numbers starts with : "))
int_To = int(input("Enter the Range of numbers ends with : "))

#Str_output = "Divisable by 6 but not by 12 between" + int_From + "and" + int_To + "are:"
print ("Divisable by 6 but not by 12 between", int_From , "and" , int_To , "are:")

for num in range (int_From, int_To + 1):
    if (num %6 == 0) and (num %12 != 0):
        print (num)
    else:
        continue

