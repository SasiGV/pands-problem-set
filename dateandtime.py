#Sasikala Varatharajan G00376470

#Program to print date time in the given format
#Monday, January 10th 2019 at 1.15pm

#Import date method from datetime module
from datetime import datetime
from datetime import time

today = datetime.today()
now = datetime.now()

#Print Date and time using given format
print(today.strftime("%A, %B %dth %Y at"), end = " ")
print(now.strftime("%#I:%M %p"))
