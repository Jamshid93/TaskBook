A=float(input("A= "))
B=float(input("B= "))
C=float(input("C= "))
if ((A>=B)and(B>=C)):
    print(A+B)
elif((B>=A)and(A>=C)):
    print(B+A)
elif((C>=B)and(B>=A)):
    print(C+B)
elif((C>=A)and(A>=B)):
    print(C+A)
elif((B>=C)and(C>=A)):
    print(B+C)
