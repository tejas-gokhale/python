# object is a thing that contains data and also has methods
# now a method in an object is pretty much like a function and uses data from that same object
# an object is a thing that has its built in attributes to describe it
# attributes: chappy.man, chappy.smart, chappy.sexy etc.
# methods: shave(), read(), eat()

# an object is based on CLASS

class exampleClass:
    eyes = "blue"
    age = 22
    def thisMethod(self):   #first param must always be self
        return "Hey this method works"

exampleObject = exampleClass()  #refers to blueprint class above
exampleObject.eyes
exampleObject.thisMethod

class className:
    def createName(self, name):
        self.name = name
    def displayName(self):
        return self.name
    def saying(self):
        print "Hello %s" % self.name

className        
first_obj = className()
second_obj = className()

first_obj.createName('bucky')
second_obj.createName('tony')

first_obj.displayName()



    
