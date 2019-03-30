#Program to find whether today starts with letter T or not

#Use datetime module to find Today
from datetime import date
#declare a string variable str_Today to store Today
str_Today = date.today()

#%A helps us to find Weekday's full name
str_Weekday = str_Today.strftime("%A")

#Sting function startswith will help us to verify whether the weekday starts 
# with the given string at the given start and end position
x = str_Weekday.startswith("T", 0, 1)

#Based on the return value of x print the output
if x == True:
    print ("Yes - today begins with a T")
else:
    print ("No - Today does not begin with a T")

print ("Today is", str_Weekday)