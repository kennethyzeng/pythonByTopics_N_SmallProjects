##Copy all the content of one file to another file in uppercase

f1 = open("sample file 1.txt", "r")
  
f2 = open("sample file 2.txt", "w")
  
# For loop to traverse through the file
for line in f1:
    f2.write(line.upper())  