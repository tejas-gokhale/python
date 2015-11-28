# strings
# both double and single quotes work
# however, consider the example: 'he's a jerk'
# the apostrophe gets treated as end of quote

# a workaround is 'he\'s a jerk'
# the backslash treats the next char as a char

a = "tejas"
b = "gokhale"

# concatenation
c = a + b

# a lot of times, you might wanna treat a number as a string
# cannot concatenate str and int

age = 22
name = "tejas is "

str_age_type  = str(age)
str_age_backticks = 'age'# type-casting is fucking easy

print(name + str_age_type)
print(name + str_age_backticks)

# how to plug in variables in your strings??
# ---------------------------------------------------------------
bucky = "Hey there %s, how's your %s" # %s stands for string
varb = ('betty', 'foot');
print bucky % varb
# output: Hey there betty, how's your foot




