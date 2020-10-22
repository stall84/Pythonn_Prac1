
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
# yields [0,0,0(96 more times), "Apples", "Oranges", etc]
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
