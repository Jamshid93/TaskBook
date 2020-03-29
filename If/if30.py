x=int(input("x= "))
if((9<x<100)and((x%2)!=0)):
    print("two-digit odd number")
elif((9<x<100)and(x%2)==0):
    print("two-digit even number")
elif ((99<x<999)and(x%2)!=0):
    print("Three-digit odd number")
elif((99<x<999)and((x%2)==0)):
    print("Three-digit even number")
elif((0<x<10)and((x%2)!=0)):
    print("one-digit odd number")
elif ((0<x<10)and((x%2)==0)):
    print("one-digit even number")