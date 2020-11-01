from sys import getsizeof

## Traditional Comprehension of List ##
values = [x * 2 for x in range(10)]
print('Values List: ', values)
# prints  Values List:  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for x in values:
    # print(x)
    pass

values_big_list = [x * 2 for x in range(1000)]
print('big list size: ', getsizeof(values_big_list))
# prints  big list size:  8856 (bytes)
# However NOTE if you're working with very large data-sets or potentially infinite datasets
## You don't want to store those values in-memory like above example. ##

# Generator Objects are iterable just like lists.  Values are generated in each iteration instead of all at once
# NOTE Although Generators save memory by iterating on-demand. They CANNOT have their length len() read like lists/arrays
values_gen = (x * 2 for x in range(10))
print('Values Generator: ', values_gen)
# prints  Values Generator:  <generator object <genexpr> at 0x7f9e300f76d0>
for x in values_gen:
    # print(x)
    pass

values_big_gen = (x * 2 for x in range(1000))
print('big generator size: ', getsizeof(values_big_gen))
# prints  big generator size:  112 (bytes)
