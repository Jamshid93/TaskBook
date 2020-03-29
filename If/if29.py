x=float(input("x= "))
if((x>0)and((x%2)!=0)):
    print("positive odd number")
elif((x>0)and(x%2)==0):
    print("positive even number")
elif ((x<0)and((x%2)!=0)):
    print("negative odd number")
elif((x<0)and((x%2)==0)):
    print("negative even number")
else:
    print("zero number")