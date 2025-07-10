import math
def ReverseInterger(x:int):
    if(x>=10):
        val = int(str(x)[::-1])
    else:
        val = -(int(str(abs(x))[::-1]))
    if(val<=-2**31 or val>=2**31-1):
        return 0
    else:
        return val
    
x= 123
y=-123
z=0
a=-2147483648
b=2147483648


print(ReverseInterger(a))
