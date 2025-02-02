#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21

import random
bot_num:int = random.randint(0,99) 

for i in range(0,10):
    
    num:int = int(input(f"Enter no. you guess you have {10-i} chance left -> "))

    if(bot_num==num):
        print("You Won The Game!")
        exit()

print("Computer guessed->",bot_num)
