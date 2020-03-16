from math import sqrt
x1=float(input("x1= "))
y1=float(input("y1= "))
x2=float(input("x2= "))
y2=float(input("y2= "))
x3=float(input("x3= "))
y3=float(input("y3= "))
a=sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
b=sqrt(((x3-x2)*(x3-x2))+((y3-y2)*(y3-y2)))
c=sqrt(((x1-x3)*(x1-x3))+((y1-y3)*(y1-y3)))
P=a+b+c
p=(a+b+c)/2
S=sqrt(p*(p-a)*(p-b)*(p-c))
print(P)
print(S)