x=float(input("x= "))
if ((x%2==0)and(x/0==0)):
    x=1
    print("f(x): ",x)
elif(x<0):
    x=0
    print("f(x): ",x)
else:
    x=(-1)
    print("f(x): ",x)