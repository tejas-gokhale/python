# CLASSES
# ****************************************
class parentClass:
    var1 = "I'm Iron Man"
    var2 = "Let's put a smile on that face"
    
    
class childClass(parentClass):
    pass

# don't want to copy everything, aka laziness

parentObject = parentClass()
parentObject.var1

childObject = childClass()
childObject.var1
childObject.var2

# the child class will inherit the parent characteristics
# ---------------------------------------
class parent:
    var1 = "bacon"
    var2 = "sausage"
    
class child(parent):
    #keep var1 the same
    var2 = "beef"

pob = parent()
cob = child()
print cob

pob.var2
cob.var2

# multiple parents
# ----------------------------------
class mom:
    var1 = "hey I'm mom!"
class dad:
    var2 = "hey there son"
class child(mom, dad):
    var3 = "am i like a new var?"
    
childObject = child()
print childObject.var1



