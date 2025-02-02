#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21

for i in range(1,6):
    print('* ' * i)
"""output ->
* 
* * 
* * * 
* * * * 
* * * * * 
"""

for i in range(1,6):
    print('* ' * (6-i))
"""output->
* * * * * 
* * * * 
* * * 
* * 
* 
"""

for i in range(1,6):
    for j in range(i,5):
        print(" ",end="")
    print('*' * i)
"""output->
    *
   **
  ***
 ****
*****
"""

for i in range(1,6):
    for j in range(i,5):
        print(" ",end="")
    print(' *' * i)
"""output-> 
    *
   * *
  * * *
 * * * *
* * * * *
"""

for i in range(1,6):
    for j in range(1,i):
        print(" ",end="")
    print(' *' * (6-i))
"""output->
* * * * *
 * * * *
  * * *
   * *
    *
"""