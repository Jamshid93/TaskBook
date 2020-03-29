A=float(input("A= "))
B=float(input("B= "))
C=float(input("C= "))
if((A>B)and(B>C)and(B<0)):
    A=A+B*(-1)
    print("nearest point: ",B)
    print("distance: ",A)
elif((A>C)and(C>B)and(C<0)):
    A=A+C*(-1)
    print("nearest point: ",C)
    print("distance: ",A)
elif((A<B)and(B<C)and(B<0)):
    A=(A+B*(-1))*(-1)
    print("nearest point: ",B)
    print("distance: ",A)
elif((A<C)and(C<B)and(C<0)):
    A=(A+C*(-1))*(-1)
    print("nearest point: ",C)
    print("distance: ",A) 