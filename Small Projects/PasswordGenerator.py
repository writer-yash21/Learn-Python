#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21

import random
class Password:
    num:str = "0123456789"
    specialsymbol:str = "!@#$%^&*"
    alphabet:str = "abcdefghijklmnopqrstuvwxyz"
    def generate(self,length:int):
        gen_password:str ="" 
        while True:
            rnum = random.randint(1,4)
            if rnum == 1 :
                gen_password += self.num[random.randint(0,9)]
            elif rnum == 2:
                gen_password += self.specialsymbol[random.randint(0,7)]
            elif rnum == 3:
                gen_password += self.alphabet[random.randint(0,25)]
            elif rnum == 4:
                gen_password += self.alphabet[random.randint(0,25)].upper()
            if length == len(gen_password):
                return gen_password
            
P = Password()
print(P.generate(10))