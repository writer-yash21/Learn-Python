#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21


# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable, and unindexed.
"""Set is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage."""

set1 = {10, 20, 30}
print(set1) # {10, 20, 30}

#length of list len()->used to find length
print(len(set1)) # 3

#Set constructor
set2 = set(("yash", "dhanush", "prabhas")) #we can crete set by using set()
print(set2)  # {'dhanush', 'yash', 'prabhas'}


# To add one item to a set use the add() method
set3 = {10, 20, 30}
set3.add(40)
print(set3) # {40, 10, 20, 30}

# To remove an item in a set, use the remove()
set4 = {10, 20, 30}
set4.remove(10)
print(set4) # {20, 30}

# Add Set
set5 = {1,2,3}
set6 = {4,5,6}
set6.update(set5)
print(set6)  # {1, 2, 3, 4, 5, 6}