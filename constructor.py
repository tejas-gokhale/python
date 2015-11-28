# constructor

# whenever you first create an object, you first need to call the methods before you can use them
# constructor: methods get called automatically

# without constructors
# ---------------------
class swine:
    print "beef pie"
    
obj = swine()
obj.apples()

# with constructor
# -------------------

class new:
    def __init__(self):         # underscore underscore
        print "this is a constructor"
        print "this also prints out"
        
newObj = new()
# this will printout everything without calling the method

    




