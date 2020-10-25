from collections import deque

## MAP FUNCTIONS ##
####################

# List of tuples for example:
items = [
    ("Product1", 22),
    ("Product2", 38),
    ("Product3", 18),
    ("Product4", 5),
    ("Product5", 8)
]
# First create an empty list to store output
prices = []
for item in items:
    prices.append(item[1])
    # appends the 2nd element of each tuple (the prices only) forms NEW list


print(prices)
# [22, 38, 18]

# Using the MAP function makes this easier
# This lambda iterates over items list and assigns the 2nd element to item keyword
lam_prices = map(lambda item: item[1], items)
# You must then loop over the returned mapped object
for price in lam_prices:
    print(price)


## FILTER FUNCTION ##
######################

# still using items list above to return/print all items greater than or equal to 20

filt_prices = filter(lambda item: item[1] >= 20, items)
for price in filt_prices:
    print(price)
# prints  ('Product1', 22)
#         ('Product2', 38)

# LIST COMPREHENSIONS ##   Signature:  [expression for in]
##########################

# Likely unique to Python.  Can substitute for MAP and FILTER by placing an expression
# in front of the loop iteration


comp_prices = [item[1] for item in items]
print(comp_prices)
# prints  [22,38,18,5,8]

comp_prices2 = [item for item in items if item[1] >= 10]
print(comp_prices2)
# prints  [('Product1', 22), ('Product2', 38), ('Product3', 18)]


####  ZIP FUNCTION  #####

# Combine two lists into a single list of tuples
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
# Zip function takes multiple iterables as it's arguments
# You can also pass an arbitrary iterable like the "ABC" string
# Below and it will be spread into the resulting tuples
zipd_list = zip("ABCD", list1, list2)
for item in zipd_list:
    print(item)
# prints: ('A', 1, 10)
#         ('B', 2, 20)
#         ('C', 3, 30)
#         ('D', 4, 40)


########  STACKS  ########
##########################
# Utilizing LIFO - Last In First Out Stacking

browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print("Browsing Session List: ", browsing_session)

# pop off the last browsing session with pop method
last_sesh = browsing_session.pop()
print("Last Sesh: ", last_sesh)
# prints Last Sesh: 3
print("Browsing Session List: ", browsing_session)
# Prints [1, 2]
# Use -1 index to return element from end of list
print("redirect: ", browsing_session[-1])
# prints redirect: 2
# Checking if the stack is empty can be done with if-not statement
if not browsing_session:
    print("disable back button")

############  QUEUES  ###########
#################################
# Utilizes FIFO in contrast to Stacks. So First In First Out
# Import the deque class at top of file
queue = deque([])
# Pass deque an empty object
queue.append(2)
queue.append(4)
queue.append(6)
print(queue)
# deque([2,4,6])
queue.popleft()
# use popleft method to pop off an element from the end of queue
print(queue)
# deque([4,6])

#############  TUPLES  #############
####################################
# Read-Only Lists

point = (1, 2)
# parens can be ommited i.e. point = 1, 2   Python will know this is a tuple
# can also use just 1 element WITH TRAILING COMMA i.e. point = 1, and python will register tuple
# You can also initiate an empty tuple like so: point = ()
# You can convert a list to a tuple by calling the tuple() function
