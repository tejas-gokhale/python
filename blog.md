*17:12 25-Nov-15*
___
# Python Features
* Scripting Language
* Enforced indentation
* High-level data-types
* Extensible
* Interpreted
---Run directly from source code, instead of translating to machine code
* Multi-paradigm

## Pythonic philosophy:
Code that identifies as *pythonic* meets the following criteria:
* includes interfaces that work well with Python
* makes good way of Python idioms

## Two ways to interact with Python
1. Interactive (line-by-line)
---includes extensive help
2. IDLE


*22:35 28-Nov-15*
___
## Lists
* Slicing
* len, del, min, max
* type-casting strings

## Classes, Methods, Objects
```
object is a thing that contains data and also has methods
now a method in an object is pretty much like a function and uses data from that same object
an object is a thing that has its built in attributes to describe it
attributes: chappy.man, chappy.smart, chappy.sexy etc.
methods: shave(), read(), eat()
```
### Built-in Methods
* append
* count
* extend
* insert
* remove
* pop
* reverse
* index
* sort
* find
* lower
* replace

### Keyword 'in'

## Constructors
whenever you first create an object, you first need to call the methods before you can use them
with **constructors**, methods get called automatically

## Parent and Child Inheritance
* child inherits parent characteristics
```
class parentClass:
	var1 = "bacon"
	var2 = "sausage"
class childClass(parentClass)
	pass
```
* child can have multiple parents
```
class mom:
    var1 = "hey I'm mom!"
class dad:
    var2 = "hey there son"
class child(mom, dad):
    var3 = "am i like a new var?"
    
childObject = child()
```

## Modules
can import modules if they are stored in the python dir
example C:\Python27\


