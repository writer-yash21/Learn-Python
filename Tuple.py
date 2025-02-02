#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21


# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.

"""Tuple is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage"""

tuple1 = (10, 20, 30)
print(tuple1) # (10, 20, 30)

#Access by index
print(tuple1[0]) # 10 
print(tuple1[2]) # 20

#Access by negative index
print(tuple1[-1])  # 30

#Range Index [start value : stop value]
print(tuple1[0:2])  # (10, 20)
print(tuple1[:1])  # (10,)
print(tuple1[1:])  # (20, 30)

#length of tuple len()->used to find length
print(len(tuple1)) # 3

#Tuple constructor
tuple2 = tuple(("yash", "dhanush", "prabhas")) #we can crete tuple by using tuple()
print(tuple2)  # ('yash', 'dhanush', 'prabhas')

#check item in Tuple
tuple3 = ("yash", "prabhas", "dulqueer")
if "dulqueer" in tuple3:
  print("Available")  # Available

#update list (we can update tuple by coverting into list)
tuple4 = (1,2,3,4)
print(tuple4)   # (1, 2, 3, 4)
# tuple4[3] = "yash" # It throw a error bcz tuple unchangeable
list1 = list(tuple4)
list1[3] = "yash"
tuple4 = tuple(list1)
print(tuple4)   # (1, 2, 3, 'yash')

# Add tuple
tuple5 = (1,2,3)
tuple6 = (4,5,6)
print(tuple5+tuple6)  # (1, 2, 3, 4, 5, 6)