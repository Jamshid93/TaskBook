x1=int(input("x1= "))
y1=int(input("y1= "))
x2=int(input("x2= "))
y2=int(input("y2= "))
x3=int(input("x3= "))
y3=int(input("y3= "))
if (x2==x3):
    x4=x1
elif(x3==x1):
    x4=x2
elif(x1==x2):
    x4=x3

if(y2==y3):
    y4=y1
elif(y3==y1):
    y4=y2
elif(y1==y2):
    y4=y3
print("x4=",x4,"\n","y4=",y4)