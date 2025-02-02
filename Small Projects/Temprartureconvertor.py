#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21

print("Welcome To Temprarture App")
temp_value:float = float(input("Enter temperature value -> "))

print("1. Celsius")
print("2. Fahrenheit ")

temp_unit:str = input("Enter temprature unit no. ")

if temp_unit == 1:
    print("Temprature in Fahrenheit is -> " , (1.8 * temp_value)+ 32 )

elif temp_unit == 2:
    print("Temprature in Celsius is -> " , (temp_value - 32)/1.8 ) 
    
else :
    print("You entered wrong value")