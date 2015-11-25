#! C:\Python27

# modifies string in scope. does not return modified string
def modify_string(original):
    original += "that has been modified in scope."

# returns modified string   
def modify_string_return(original):
    original += "that hath been modified."
    return original

test_string = "Is a test string this"
modify_string(test_string)
print(test_string)

test_string = modify_string_return(test_string)
print(test_string)
