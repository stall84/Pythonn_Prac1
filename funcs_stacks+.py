

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
