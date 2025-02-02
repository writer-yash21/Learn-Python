#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21

# BASIC OF PYTHON

# <- THIS IS COMMENT
"""THIS IS MULTILINE COMMENT"""

# hello world program
print("Hello World") # Hello World

#Variable
x = 5
print(x) # 5
x = "yash"
print(x) # yash

#Basic Data types
x = 5      #int
x = "YASH" #string
x = 19.90  #float
x = True #bool
x = [1,"yash",True] # List like Array in C/C++
x = (1,2,3,4,5) # Tuple
x = {"yash","Dhanush","krishna"} # Sets
x = {
    "name":"yash",
    "age" : 19
}   # Dictionary

#Arthmetic operators
w = 5 + 2 # addition
x = 5 - 2 # substract
y = 5 * 2 # multiply
z = 5 / 2 # divide
print(w,x,y,z) # 7 3 10 2.5

#Standard Input
x = input("Enter anything \n")
print(x)  # print value of x entered by keyboard

#Data type-conversion (type() -> function is for show data type )
x = int("123")
print(type(x)) # <class 'int'>    

x = str(123)
print(type(x)) # <class 'str'>

#control flow (if , else , elif)
x = int(input("Enter number \n"))  # int()->it convert string to number 

  
if(x%2 == 0):  # if-else
    print("even") # if x is even it print "even"
else:
    print("odd")  # if x is odd it print "odd"


if(x>0):      # if-elif-else
    print("postive")
elif(x<0):
    print("negative")
else:
    print("zero")

#Logical operator 
if( True and True):  # and -> Run when both are true
    print("Both are true")
if(False or True):
    print("One is true")  # or -> Run when one of them is true
if(not False):
    print("False to true")  # not -> convert True to false or vice-versa  


#loops(for , while)
x = 0
while(x < 5):
    print(x,end= " ")  # 0 1 2 3 4
    x += 1

for i in range(0,5):    # range() -> function is used to generate list from given start and end point 
    print(i,end=" ") # - 1 2 3 4 


#Basic function
def greet():     #define the greet function
    print("hello world") # hello world
greet() # calling the greet funtion
