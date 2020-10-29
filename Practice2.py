

#######################  FUNCTIONS  #########################

# Start functions with keyword def
# In python you can return multiple values as long as they're
# enclosed in parenthesis and sep'd by comma
# default values can be defined for parameters. In example below, if no argument is
# given at function call.. it will default to incrementing by 1
def incrementer(number, by=1):
    return (number, number + by)


# (2, 5) : this returns a tuple .. A read-only list of sorts
# further: python allows keyword arguments to make code even more
# readable. In example below, 2 incremented BY 3
print(incrementer(2, by=3))  # Returns (2,5)
print(incrementer(2))   # Returns (2,3)

#####################  ARBITRARY # OF ARGUMENTS ######################
# If you want to make a function with an undefined/arbitrary number of input
# parameters. Use asterik * and python will create a tuple of that list or
# whatever function you want to do on it


def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))    # Returns 120

######  Variation on above arbitrary args  #########
# Using keyword arguments. Returns what python calls a 'DICTIONARY',
# but which is very similar to a javascript object (json more specifically)


def save_user(**user):
    print(user)


print(save_user(id=1, name='admin'))    # Returns {'id':1, 'name': 'admin'}

######################  SCOPE IN PYTHON  #####################
# LOCAL VARIALBES - FUNCTION SCOPE
# GLOBAL VARIABLES - FILE SCOPE

# Unlike javascript, THERE IS NO BLOCK-LEVEL SCOPING .. So if message were within an inner 'if' block,
# it will still be available to rest of function.


def greet():        # message is local scoped to greet function
    message = 'a'


# Glboal variables accessible anywhere in file, any functions therein
message_global = 'sup'


def greeting():
    print(message_global)


greeting()


##  DEBUGGING ##
# In vs-code .. same as other languages, set a breakpoint and open panel
