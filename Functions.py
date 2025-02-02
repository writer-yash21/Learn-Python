#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21


#Basic function
def greet():     
    print("hello world") # hello world
greet() 

#function with argument
def greet(name):
    print(f"hello {name}") # hello yash
greet("yash")

#default argument function
def greet(name="no name"):
    print(f"hello {name}") 
greet("yash") # hello yash
greet() # hello no name

# return function
def add(a,b):
    return a+b
print(add(1,2)) # 3
print(add("yash ","jangid")) # yash jangid

# Some functions 

def check(n):
    if n%2 == 0:
        return "even"
    return "odd"
print(check(21)) # odd
print(check(26)) # even

def palindrome(x):
    if x == x[::-1]:
        return "Palindrome"
    return "Not Palindrome"
print(palindrome("122")) # Not Palindrome
print(palindrome("121")) # Palindrome

def armstrong(x):
    n = x
    res = 0
    while(x > 0):
        rem = x%10
        res = res+ (rem*rem*rem)
        x = x // 10
    if n == res:
        return "armstrong"
    return "not armstrong"
print(armstrong(123)) # not armstrong
print(armstrong(153)) # armstrong