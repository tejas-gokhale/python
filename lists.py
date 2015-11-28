family = ['mom', 'dad', 'bro', 'sis', 'dog']
family[3]

family[-2]

# python allows you to count backwards
# 0 , 1 , 2 , 3 , 4
# -5, -4, -3 ,-2 ,-1


# slicing
example = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
example[4:8] # gives elements 4 to 7
# [4:10] gives the end

example[-5:0] #does not work
example[-5: 1] #does not include all

example[:7] # zeroth to sixth
example[5:] # fifth to last

'bucky'*10 #gives you repetitions 

name = 'roastbeef'

# built-in keyword 'in'
'z' in name
'r' in name

'cat' in family
'mom' in family

# length, max, min functions
len(example) #straight and easy
max(example)
min(example)

# list function
list('chappy')  # lists all char in string in a list

# del function
del examples[5] #deletes element 5 and now the list has only 9 elements

# slicing lists
example[1:1] = [3, 3, 3] #has the following outcome
# example == [0 3 3 3 1 2 3 4 5 6 7 8 9]
 



