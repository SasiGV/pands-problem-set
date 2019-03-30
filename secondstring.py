#Program to print every second word from the given input

#Get input from the user
Str_Input = input("Please enter a sentence: ")

#Using string module and split method splits all the words from the given sentence.
#This mehtod will convert the values into List
Lst_Input = Str_Input.split()

#Initialize variable i with value 1
i = int(1)

#Find the number of items from the List
n = (len(Lst_Input))

#Print the first word from the given sentence
print(Lst_Input[0], end = " ")

#Loop until the last item in the list to print every second word
while i <= n-1:
    if (i % 2 == 0):
        print(Lst_Input[i], end = " ")
    i += 1
