# Problem set 'pands-problem-set' Solutions

Name : Sasikala Varatharajan 
Student Number : G00376470

This repository contains my solutions to the Problems included in the First assignment Problem-set 2019 for the module Programming and Scripting at GMIT
[See here for the instructions](https://web.microsoftstream.com/video/2d4fec98-175e-4a12-a07e-bd096f40fc3c)

#How to download this repository
1. Go to GitHub
2. Click the 'Clone or Download' button
3. Click on Download as Zip

#How to run the code
1. If you do not have Python installed then [download](https://www.anaconda.com/distribution/) it from this link and install it
2. Visual Studio code will be very usefull to view the code and you can get it from this [link](https://code.visualstudio.com/)

#Contents of this Problem Set
Based on the instructions from the Problem set you can find solution for each program listed below

1. sumupto.py

    This program will get a positive integer from the user and calculate the total of numbers starting from 1 to the number entered. 
    eg. If the user enters 10 then it will start to add all the numbers between 1 and 10 using a for loop.
    So the output will be 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
    
    ##References

    [For Loop in Python](https://docs.python.org/3/tutorial/controlflow.html)

2. begins-with-t.py

    This program will use datetime module to find today and time. Based on the findings it will then print whether today starts with T or not.
    Startswith mehtod from String module helps us to verify the string starts with the given letter or letters based on the start and end position arguments.

    ##References

    [startswith](https://docs.python.org/3/library/stdtypes.html?highlight=startswith#str.startswith)

3. divisors.py
    
    This program will get two inputs lower and upper limit of the interval to find the numbers that are divisable by 6 but not by 12.
    Using modulus operator we can filter the numbers are divisable by 6 but not 12.

    ##References
    [Modulus](https://www.programiz.com/python-programming/operators)

4. Collatz.py

    This program will get a positive integer from the user and prints the sucessive values of the given calculation. If the given value is even then it will divide it by 2 and if it is odd then it will be mulitiplied by 3 and incremented by 1.
    Using modulus we can differentiate even and odd numbers. In order to print successive values I have used end = " " argument with print statement which will take a space instead of new line.

    ##References
    Using [end] parameter (https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/) 

5. primes.py

    This program will find whether the given number is prime or not.
    Prime numbers is divisable by itself and 1 only and they are greater than 1. This program will get a positive input value from the user and figures out if it is divisable by any one of the number between 2 and the given number. If the program can find any other divisor between 2 and the given number then it will print that the given number is a Prime number. Otherwise it will print the first divisor of the given number as a proof of why it is not a prime number.

6. secondstring.py

    This program will get an input string from the user and prints every second word from the first onwards.
    It uses split method from string module to split every word from the given string and stores them in a list. Using a for loop we can find out words resides at even position in the list and the end=" " parameter in the print statement will help us to print the words in successive order.

    ##References
    [List](https://www.tutorialspoint.com/python/python_lists.htm)

7. squareroot.py

    This program will print the squareroot of the given number. It uses math module and one of the method math.sqrt will help us to find the squareroot of the value. 
    Here I have converted the input value as float as most of the numbers will have fraction number as output. Before printing the output it will verify the whether the output is integer or not. If it is integer then it will print it without decimals and if it is not then it will print the output with 2 decimal places.

    [Is_integer](https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not)

8. dateandtime.py

    Since the datetime module conflicts with the name of the program I have changed the name of it to dateandtime.py. This program will find todays date and time and print it in the given format. eg. Monday, January 10th 2019 at 1.15pm.

    ##References
    [datetime](https://www.programiz.com/python-programming/datetime)

9. second.py

    This program used commandline argument to get input file name from the user. I have created a text file called moby-dick.txt as said in the instructions and stored in the base location of the program.

    In order to avoid the decode error message I have used encoding parameter while reading the file. 

    This program will read the input file and it will print every second line from the first line onwards.

    ##References
    [encoding](https://stackoverflow.com/questions/30750843/python-3-unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d?noredirect=1)
    Help to [read] a file. (https://stackabuse.com/read-a-file-line-by-line-in-python/)

10. mymatplot.py
