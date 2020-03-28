A=float(input("A= "))
B=float(input("B= "))
if (A>B):
    B=A
elif(A<B):
    A=B
else:
    A=0
    B=0
print(A,"\n",B)