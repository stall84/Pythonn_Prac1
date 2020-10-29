from array import array

####  SWAPPING VARIABLES  ######
################################

# Below is the manual way of swapping variables (You have to bring in a 3rd temporary variable)
x = 10
y = 50

z = x
x = y
y = z

print('x', x)
# x 50
print('y', y)
# y 10

# Python gives us a much nicer, more clever way of doing it w/o 3rd variable

x2 = 10
y2 = 50

x2, y2 = y2, x2
# Python makes the right side of the operator a TUPLE .. x2, y2 = (11,10)
# Since Python makes the right side a tuple.. the statement becomes an unpacking event
# making y2= 10 and x2 = 50
# This same principle allows you to define multiple vars on the same line

print('x2', x2)
print('y2', y2)


########  ARRAYS  #########
###########################

# Array's take up less memory and work a little faster .. Usually you want to use lists
# But if you're working with very large numbers of elements .. Try using arrays
# must be imported from array module

# Call as a function/method # The first argument is a TYPECODE string
# NOTE These are strong-typed, only same type allowed
# This is a string that defines the type of array https://docs.python.org/3/library/array.html

# signed integer array = 'i' typecode
number_arr = array('i', [50, 100, 150, 300, 600, 6000])
# Same methods used on Lists can be used on Arr's, .. Like append, insert, pop

popd = number_arr.pop()

print('number_arr: ', number_arr)
print('popd: ', popd)
# 6000


#######   SETS  ########
########################
# Collections with NO DUPLICATESA
nums_2 = [1, 1, 2, 3, 4, 4, 4, 5, 6]

uniques = set(nums_2)
print('uniques', uniques)
# prints  {1,2,3,4,5,6   NOTE Sets use curly brace syntax}

# Defining a set outright use curly brace syntax. add, len, remove, methods can be used
set_2 = {1, 5, 10, 20}
set_2.add(1000)
print(set_2)
# Sets become powerful when doing math or other operations like joins/unions
# Sets are unordered .. You can't index them like set[0] to get first element

# Joins
print(uniques | set_2)
# {1, 2, 3, 4, 5, 6, 1000, 10, 20}

# Intersection
print(uniques & set_2)
# {1, 5}

# Difference
print(uniques - set_2)
# {2, 3, 4, 6}

# Symetric Sets (Either in one or the other, but not both)
print(uniques ^ set_2)
# {2, 3, 4, 6, 1000, 10, 20}


##########  DICTIONARIES  ############
#######################################
# Key Value Pair Collection
# Similar to Objects in other langauges
# NOTE The KEY must be an immutable type, so usually you'll see strings, numbers ..
# The VALUE though can be anything (immutable or not)

point = {"x": 1, "y": 2}
# Above is a basic dictionary

# The dict() function can also be used to construct a dictionary
# To get the value. Use the index of the key (different from objects in other languages
# where you could just dot-notate the key)

point2 = dict(x=3, y=4)
print(point2["x"])
# 3
# similar to objects values can  be changed with brace notation
point2["y"] = 55
print(point2)
# {'x': 3, 'y': 55}
# You can also add a new key with braces
point2["z"] = 105
print(point2)
# {'x': 3, 'y': 55, 'z': 105}

# To Loop over a Dictionary you'll need to use the signature
# because the default behavior is to only iterate over the keys
# for key in point:
# print(key, point[key])
for key in point2:
    print(key, point2[key])
# x 3
# y 55
# z 105


############  DICTIONARY COMPREHENSIONS  #############
######################################################

#  To review the signature for (List) Comprehension:
#  [expression for item in items] where we iterate over an iterable (items) and for each item
#  we do something to it (expression)
values = []
for x in range(5):
    values.append(x * 2)

print('Values: ', values)
# Values:  [0, 2, 4, 6, 8]
#  ^^^ To Transform to a comprehension:
values_compd = [x * 2 for x in range(5)]
print('Compd Values: ', values_compd)
# Compd Values:  [0, 2, 4, 6, 8]
# Of note you can use comprehensions with sets by using curly braces {expression for item in items}
# you can also use comprehensions for dictionaries, also by utilizing curly braces

compd_dic = {x: x * 2 for x in range(5)}
print('Compd Dic: ', compd_dic)
# Compd Dic:  {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
