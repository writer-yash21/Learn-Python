#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21

#Lists are used to store multiple items in a single variable.
#List items are ordered, changeable, and allow duplicate values.
"""Lists are one of 4 built-in data types in Python used to store collections of data
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage"""

list1 = [1,"yash",True]
print(list1) # [1, 'yash', True]

#Access by index
print(list1[0]) # 1 
print(list1[2]) # True

#Access by negative index
print(list1[-1])  # True

#Range Index [start value : stop value]
print(list1[0:2])  # [1, 'yash']
print(list1[:1])  # [1]
print(list1[1:])  # ['yash', True]

#length of list len()->used to find length
print(len(list1)) # 3

#list constructor
list2 = list(("yash", "dhanush", "prabhas")) #we can crete list by using list()
print(list2)  # ['yash', 'dhanush', 'prabhas']


#check item in list
list3 = ["yash", "prabhas", "dulqueer"]
if "dulqueer" in list3:
  print("Available")  # Available


#update list
list4 = [1,2,3,4]
print(list4)   # [1, 2, 3, 4]
list4[3] = "yash"
print(list4)   # [1, 2, 3, 'yash']


#update in a range
list5 = ["yash", "krishna", "arjun"]
list5[1:3] = ["prabhas","kalki"]
print(list5)  # ['yash', 'prabhas', 'kalki']

# The insert() method inserts an item at the specified index
list6 = [10,20,30]
list6.insert(2, 15)
print(list6) # [10, 20, 15, 30]



# To add an item to the end of the list, use the append() method
list7 = [10,20,30]
list7.append(15)
print(list7) # [10, 20, 30, 15]

# The remove() method removes the specified item
list8 = ["apple", "banana", "cherry"]
list8.remove("banana")
print(list8) # ['apple', 'cherry']

# The pop() method removes the specified index
list9 = [11, 22, 33]
list9.pop(1)
print(list9) # [11, 33]


# The del keyword can also delete the list completely
list10 = [1,2,3,4,5]
del list10
# print(list10) <- throw a error because list10 is deleted


# The clear() method empties the list
list11 = [12, 13, 14]
list11.clear()
print(list11) # []

# List objects have a sort() method that will sort the list alphanumerically, ascending or decending
list12 = ["yash", "angraaz", "meera", "adhura"]
list12.sort() 
print(list12) # ['adhura', 'angraaz', 'meera', 'yash']
list12.sort(reverse=True)
print(list12) # ['yash', 'meera', 'angraaz', 'adhura']

# Add list
list13 = [1,2,3]
list14 = [4,5,6]
print(list13+list14)  # [1, 2, 3, 4, 5, 6]