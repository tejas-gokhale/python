def whatsup(x):
    return 'what\'s up ' + x

print whatsup('noob')

# tuple *
# ----------------------------------------
def list(*food): #treat food as a tuple
    print food

list('apples', 'peaches', 'beef')

def profile(name, *ages): #ages can have any no. of parameters as it can
    print name, ages

# dictionary ** (items and values)
# -------------------------
def cart(**items):
    print items

cart(apples = 4, peaches = 6, beef = 60)

def profile(first_name, last_name, *girls_ages, **food_items):
    print first_name, last_name
    print girls_ages
    print food_items
    
profile('bucky', 'roberts', 32, 22, 17, 23, 20, bacon = 4, sausage = 64)

    