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

# Escape sequences in Python are the same as in other languages : \ (backslash)

print("Hello \"World\"")

# Formatted Strings (use f character) .. you can call any expression/function/method within the brackets
# very similar to js

fist_name = "Michael"
last_name = "Stallings"
full_name = F"{fist_name} {last_name}"
print(full_name)

###########  USEFUL STRING METHODS  #############

course_2 = "   Python Programming"

# UPPER()
print(course_2.upper())  # PYTHON PROGRAMMING
# LOWER()
print(course_2.lower())  # python programming
# TITLE()
print(course_2.title())  # Python Programming
# STRIP() - removes whitespace from around the string notice the whitespace in course_2 above
# (also have lstrip for left whitespace and rstrip for right)
print(course_2.strip())  # Python Programming
# FIND() - locate index of input - is case sensitive
print(course_2.find("Pro"))  # 10
# REPLACE(what,with) - 2 params, obj replacing, obj with to replace - case sensitive
print(course_2.replace("P", "-"))           # -ython -rogramming
# IN OPERATOR - really a function call taking the prefix and searching for it in the postfix
# - returns Boolean, case sensitive - can also be prefixed with NOT keyword to act like ! in js
print("Programming" in course_2)


##########  USEFUL NUMBER METHODS  ##########

# Binary representation with '0b' operator
d = 0b10  # 0010 in binary is 2
print("binary rep of 0b10: ", d)
print(bin(5))  # 0b1101
# Hexadecimal representation with '0x' operator
k = 0x12c
l = 350
print(k)  # 300 in decimal
print(hex(l))  # 0x15e
# In python j represents imaginary number (i) for complex number use


###########  ARITHMETIC OPERATORS  ############

# Same as other languages save for:
ans = 10 / 3                # Will yield a floating point number
print(ans)                  # 3.33333333333333
ans_int = 10 // 3            # Yields an integer
print(ans_int)              # 3
# Exponents
ans_exp = 10 ** 3
print(ans_exp)              # 1000
# Augmented operators same as other languages
did = 5
did += 6                    # same as did = did + 6
print(did)


#############  TYPE CONVERSION  ################

# Convert String to Number
# Python is strongly typed in that you have to explicitly tell which type to use (Not static typing)
# In comparison Javascript is Weakly-typed.. and as you know will perform type conversions on it's own

# Example
# x = input("x: ")
# y = x + 1
# Running the above will type error because python doesn't know whether to do a string conversion and yield 11
# or a number conversion and yield 2

# type conversion functions :
#  int()
#  float()
#  bool()
#  string()

k1 = 1
print(float(k1))


############## TRUTHY  FALSIES  $##################
# FALSY VALUES #
#  ""  (empty string) #
#  0  (zero) #
#  []  (empty list #
#  None (like null) #

# Everything else is Truthy

########  CONDITIONAL STATEMENTS  ##########
age = 36
# No longer need braces, pressing enter after colon will auto-indent
# Do not mix tabs and spaces. Use 4 spaces in lieu of tabs for Python3
if age >= 20:
    print("Adult")

#########  LOGICAL OPERATORS  ########
# and, or, not
name_new = ""

if not name_new:
    print("Name is Empty")

if age >= 18 and age < 65:
    print("Eligible")

# The above can be written much more cleanly as:
if 18 <= age < 65:
    print("Eligible")
