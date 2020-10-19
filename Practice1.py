#########  VARIABLES ###########

# PRIMATIVE TYPES PYTHON: INTEGER, FLOAT, BOOLEAN, STRING

# Python variables are not defined in advance of their assignment .. no var/let whatever
# Python convention on multi-word variables is snake-casing

students_count = 1000                   # Integer

rating = 4.95                           # Float

is_published = True                    # Boolean - note the upper-casing of first char

# String - can use either double or single quotes
course_name = "Python"

# Multiline string using triple quotes
course_description = """                
Multiple Lines 
Can Easily Be 
Written With 
Triple Quotes
"""

# Multiple variables can be assigned on the same line using commas to sep variables and values
x, y = 1, True


# TYPING ###############$$$$$$$$$$$$$$$$$$$

# As is true with Javascript, another dynamic-typed language.
age = 20
# Reassigning variable to different type is allowed like here int to string
age = "Python"

# Python 3.6 Allows 'type-painting' of variables allowing annotation

new_age: int = 36

# Running id method will show location in memory of stored value

x = 2

print(id(x))                        # ex:   140189343344976

# Primitives in Python like in Javascript are Immutable. Values can be reassigned to new variables
# But the original primitive itself cannot be mutated. Example below showing memory addresses with id method

y = 7
print("1st Y Pass: ", id(y))        # 140460597373424
y = 10
print("2nd Y Pass: ", id(y))        # 140729569700432
# Python's interpreter will eventually release the unused memory location after reassignment
# via Garbage-Collection

# Mutable types like Lists can mutate the same/original memory address.

list1 = [1, 2, 3, 4, 5]
print("List1 location initial: ", id(list1))            # 140484219793024
list1.append(6)
print("List1 location mutated: ", id(list1))            # 140484219793024


#####################  STRINGS  ########################

course = "Python Programming"

# length (len) function/method
print(len(course))                                      # 8
# BRACKETING FUNCTIONS
print(course[0])                                        # P
# negativing from end of string
print(course[-2])                                       # n
# Slicing - Start and end indexes required:
# [start : end] sep'd by colon
print(course[0:3])                                      # Pyt
