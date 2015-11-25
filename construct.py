#! C:\Python27

import sys
target_int = raw_input("How many integers?")

# User input is a string. Need to convert it to int or print error
try:
    target_int = int(target_int)
except ValueError:
    sys.exit("Please enter an integer")

print(target_int)    
ints = list()
count = 0
print(count < target_int)

# Ask for no. of integers specified by target_int
while count < target_int:
    new_int = raw_input("Please enter integer:".format(count + 1))
    isint = False
    try:
        new_int = int(new_int)
        isint = True
    except:
        print("Please enter an integer value")
    
    if isint == True:
        ints.append(new_int)
        count = count + 1
 
    print(count)       
print("Using a for loop")
for value in ints:
    print(str(value))

# or using a while loop
print("Using a while loop")
total = len(ints)
count = 0
while count < total:
    print(str(ints[count]))
    count += 1
    
