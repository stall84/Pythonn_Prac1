
######################  LISTS  #########################

# Within square brackets, you can have any type of object in list:
# strings, nums, bools, or more lists

string_list = ["Apples", "Oranges", "Strawberries", "Lemons"]


# returns: String List:  ['Apples', 'Oranges', 'Strawberries', 'Lemons']
print("String List: ", string_list)

matrix_list = [[0, 1], [2, 3]]

# Use asterisk on lists to repeat the items in that list
zeros = [0] * 100
print("Zeros: ", zeros)     # returns [0,0,0 ...]

# Python dynamically allows different types to reside in the same list
combined_lists = zeros + string_list
# prints [0,0,0(96 more times), "Apples", "Oranges", etc]
print("Combined Lists: ", combined_lists)

# recall that range() function returns an iterable object that can be looped or iterated over
# list() function returns a list of whatever is argued to it
numbers_list = list(range(20))
print("Numbers List: ", numbers_list)   # returns: Numbers List: [0,1,2,...,19]

letters_list = list("Hello World")
print("Letters List: ", letters_list)   # returns: Letters List: [H,e,l...]

###############  ACCESSSING ITEMS  ###############

# Similar to C languages / javascript .. use square brackets
# Using a negative number will return from end inward
# Lists can be altered/assigned same as objects in js .. with brackets
# A list can be sliced with brackets and begin colon end [begin:end]
# - WILL RETURN A NEW LIST w/o mutating orig

new_letters_list = ["a", "b", "c", "d"]
new_letters_list[1] = "B"
print(new_letters_list[0])   # returns a
print(new_letters_list[1])   # returns B
print(new_letters_list[0:3])    # returns [a,B,c]

################  LIST UNPACKING (DESTRUCTURING)  ##################

# Similar to destructuring objects or arrays in javascript, you can unpack the elements of
# a list like so:
numbers = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 7, 8, 9, 10]
numbers_min = [1, 2, 3, 4]

# Unpacking. Left side must consist of same number of variables as members in list
first, second, third, fourth = numbers_min

print(first, second, third, fourth)     # prints 1 2 3 4

# If you want to get just a portion of a list you can declare those variables on the left
# and then use asterisk to pipe/pack the remaining elements into a new list you define after it
# example below establishes 3 variables to unpack to and a new list named 'other' to send everything
# else to
first1, second1, third1, *other = numbers
print(first1, second1, third1, other)       # prints 1 2 3 [4,4,4...]

################  LIST LOOPING  #################
# for loop works same as js
letters = ["d", "h", "k", "L", "N", "o", "W"]
for letter in letters:
    print(letter)
# you can also output iterable tuples by using 'enumerate' keyword
# This will yield tuples like (0, 'd') (1, 'h') (2, 'k')... which effectively indexes the elements
for letter in enumerate(letters):
    print(letter)
# above can be further formatted by unpacking the tuple iterable like so:
for index, letter in enumerate(letters):
    print(index, letter)                    # prints 0 d  1 h  2 k ...


################  ADDING/REMOVING ELEMENTS TO LIST ##############
# Add using dot notation with append method
letters.append("Qi")
print("After appending letters list: ", letters)
# prints After appending letters list:  ['d', 'h', 'k', 'L', 'N', 'o', 'W', 'Qi']

# Insert method takes index as first argument and element to be inserted as 2nd
letters.insert(3, "-")
print("Letters List after Insert: ", letters)
# prints Letters List after Insert:  ['d', 'h', 'k', '-', 'L', 'N', 'o', 'W', 'Qi']

# To remove object with remove method you could use POP method to pop off the last element
# You can also argue an index on POP method to pop off specific element
letters.pop(2)
print("Letters after Pop(2): ", letters)
# prints Letters after Pop(2):  ['d', 'h', '-', 'L', 'N', 'o', 'W', 'Qi']
# If you want to remove an element but don't know it's index use REMOVE method arguing element to remove
letters.remove("-")
print("Removed -: ", letters)
# CLEAR method removes all elements from list

#############  FIND INDEX OF ELEMENT IN LIST ##############
print(letters.index("N"))           # 3

# Use IN operator to find/return index of element if you don't know if it's present or not to prevent error
if "o" in letters:
    print(letters.index("o"))       # 4  and no error if not in list

###########  SORTING  LISTS  ############

jumbled_nums = [18, 29, 3, 18, 2, 99, 1490, 5, 88]

# Sorts ascending by default
# NOTE You must sort the list in-place on it's own and then work with the original list
# print(jumbled_nums.sort()) will NOT work
jumbled_nums.sort()
print("Sorted List: ", jumbled_nums)
# Sorted List:  [2, 3, 5, 18, 18, 29, 88, 99, 1490]
# Use a parameter keyword to sort in diff way, reverse for example:
jumbled_nums.sort(reverse=True)
print("Reverse Sorted List: ", jumbled_nums)
# Reverse Sorted List:  [1490, 99, 88, 29, 18, 18, 5, 3, 2]
# NOTE Use the sorted() built-in function to return a NEW list after sorting without
# affecting original list
# Using this function DOES allow the following:
print(sorted(jumbled_nums))

#####  SORTING COMPLEX LISTS  #######
# You must define a function for sorting complex lists. Very similar to using
# uder-defined callbacks in javascript array methods like .map or .filter
complex_list = [("Product1", 108), ("Product2", 33), ("Product3", 105)]
# consider we want to sort these tuples in the list by their numeric price..
# use bracket notation and return the numbers by themselves.. Now Python can sort like usual


def sortem(item):
    return item[1]


# Next you simply call the sort method on the list by passing the function we defined
# as the sort argument. NOTE You must specify a keyword argument for the function parameter (key=)
complex_list.sort(key=sortem)
print("Func Sorted List; ", complex_list)
# prints Func Sorted List;  [('Product2', 33), ('Product3', 105), ('Product1', 108)]


################  LAMBDA EXPRESSION/FUNCTIONS  ################
# Signature for a lambda expression in a sort operations (taking above and making cleaner)
complex_list.sort(key=lambda item: item[1])
print("Lambad'd Sort: ", complex_list)
# Func Sorted List;  [('Product2', 33), ('Product3', 105), ('Product1', 108)]

###############  MAP  FUNCTION  ################
# Works similar to javascript in that it takes a lambda 'callback'

prices = []
for item in complex_list:
    # most basic way of achieving is to open an empty list, loop over the
    prices.append(item[1])
    # iterable, then append-on to that empty list the value in the 2nd poisiton [1]
# A better way to do this is with MAP function
# Map takes a function (lambda) and one or more iterables (lists)
# Using a lambda expression we want the 2nd element from the complex list list
mapd_list = map(lambda item: item[1], complex_list)
# This returns an iterable .. can be destructured further before
print("Lambdad Map of List: ", mapd_list)
for item in mapd_list:
    print(item)
# prints 33  105  108
# If you want to create a new list in lieu of output values, wrap the map in a list built-in function
# mapd_list = list(map(lambda item: item[1], complex_list))
