#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21


# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
"""Dictionary is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Tuple, and Set, all with different qualities and usage."""

dict1 = {
  "name": "yash",
  "age" : 19
}
print(dict1) # {'name': 'yash', 'age': 19}


#Access by Key
print(dict1["name"]) # yash
print(dict1["age"]) # 19


#Dictionary constructor
dict2 = dict(name = 'dhanush', movie_name = "Tere ishq mein") #we can crete dict by using dict()
print(dict2)  # {'name': 'dhanush', 'movie_name': 'Tere ishq mein'}

#update Dictionary
dict3 = {
  'name': 'dhanush',
  'movie_name': 'Tere ishq mein',
  'year': 2024
}
dict3["year"] = 2025
print(dict3) # {'name': 'dhanush', 'movie_name': 'Tere ishq mein', 'year': 2025}