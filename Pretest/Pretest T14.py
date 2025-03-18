#import math module and call factorial()
#solution accepts integer input
#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is >100

import math

userint = int(input())
factorial = math.factorial(userint)

if factorial > 100:
    newbool = True
    print(factorial)
    print(newbool)
elif factorial < 100:
    newbool = False
    print(factorial)
    print(newbool)