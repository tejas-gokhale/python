___
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

___
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
```python
class parentClass:
	var1 = "bacon"
	var2 = "sausage"
class childClass(parentClass)
	pass
```
* child can have multiple parents
```python
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

## Working with files
	
file object allows us to perform actions on a file
mode: 'w' or 'r' i.e write or read
```python
fob = open(<path>, <mode>)
```
```python
fob.write('hey now brown cow')
fob.close()
fob.read(bytes_to_be_read) 	# part of the file
fob.read()			# read entire file
fob.readline()			# reads upto the first break
fob.readlines()			# reads line by line
```

save each line as a string in a variable
```python
listme = fob.readlines()
fob.close()
```
*now we can edit this list* However this does not update the file obviously
**How do I edit the file?**
```python
fob.writelines(listme) # easy!
```

# GUI with Python
Install wxPython from [wxpython.org](http://www.wxpython.org/download.php)
check this [script](https://github.com/tejasG53/python/blob/master/wxBasics.py) for a basic tutorial on using wxPython

___
*00:10 30-Nov-15*
___
## Importing modules
1. You can import a module 
```python
import blahmodule
```
2. or can import part of a module
```python
from blahmodule import
```
3. **Listing the contents of an imported module**
```python
import math
dir(math)	#lists the names (functions and constants) that have been defined inside math module
help(module_name.function_name) #interactive help for a module's functions
```

___
*23:10 30-Nov-15*
___
# Basic Elements and Syntax
python does not have 'variables', instead it has '**names**'
1. ### NAME:
> In Python, a ***refers*** to an object. It is actually a label for a memory location that stores things.
> These *things* are called ***objects***
> Thus `x = 5` is read as *binding a name(x) to an object(5)*
> Names can start with _ or alphabet

Convention: use *lowercase* for names that stand for values

2. ### STATEMENTS AND EXPRESSIONS

   1. **Literal**: Chunk of text that specifies values.
   2. **Statement**: Command to do sth. (Good practice to always assign a name to a literal using a statement.)
   3. **Expression**: One or more operations that produce a result.

```python
"monty python"		#literal
x = "monty python"	#statement
print x			#expression
```

3. ### SEQUENTIAL DATA
Types:

   * Lists: 		arrays
   * Tuples: 		immutable lists
   * Strings: 		immutable, store text or binary data
   * Dictionary:	items and their values `family = {"dad": "57", "mom": "52"}`
   * sets: 		each item in a set must be unique
   * files: 		to work with files on your computer

4. ### METHODS
Data types have methods.
Each data type has built-in actions associated with it which let you do stuff to your data
These actions are called methods

   1. Calling a method
   ```python
   bleh = "Blah"
   bleh.lower()
   ```

5. ### DOCSTRING
Use docstrings to help others understand your code. They work with python's help utility so that people can figure out what your code does, without looking at the actual file.
A docstring is always the first line in a function.
```python
def function_name(parameters):
	"""
	this text is help for function_name
	"""
```

6. ### CLASSES
A class is both a factory and a blueprint: it makes copies of itself, but the copies do the actual work.
```python
class SayMyName:
	def __init__(self, myname):
		self.myname = myname
	def say(self):
		print "Hello, my name is ", self.myname
```
You can use a calss to create objects called ***instances*** that can do specific things
```python
name1 = SayMyName("chappy")
```
An instance has access to the class's *methods*
```
name1.say()	#output: Hello, my name is  chappy
```

















