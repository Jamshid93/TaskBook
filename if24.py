import math
x=float(input("x= "))
if(x>0):
    x=2*math.sin(x)
    print("f(x): ",x)
elif(x<=0):
    x=6-x
    print("f(x): ",x)
