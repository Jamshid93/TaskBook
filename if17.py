A=float(input("A= "))
B=float(input("B= "))
C=float(input("C= "))
if ((A<=B)and(B<=C)or(A>=B)and(B>=C)):
    A=A*2
    B=B*2
    C=C*2
else:
   A=A*(-1)
   B=B*(-1)
   C=C*(-1)
print(A,"\n",B,"\n",C)