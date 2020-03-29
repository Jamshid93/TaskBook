A=int(input("A= "))
B=int(input("B= "))
C=int(input("C= "))
D=int(input("D= "))
if((A==B)and(B==D)):
    C=3
    print(C)
elif((B==C)and(C==D)):
    A=1
    print(A)
elif ((A==C)and(A==D)):
    B=2
    print(B)
elif ((A==B)and(B==D)):
    D=4
    print(D)