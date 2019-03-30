#Program to get a filename as an argument. Read and output every second line.

#Import sys module to handle command line arguments
import sys

#Initialize a variable to find the number of line
i=0

#Loop through each line in the text file
with open (sys.argv[1], encoding="utf8") as fp:
   #Print every second line 
    for i, line in enumerate(fp):
       if i % 2 == 0:
           print (line)
    i += 1
    fp.close()