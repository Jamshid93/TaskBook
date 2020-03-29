A=float(input("A= "))
B=float(input("B= "))
C=float(input("C= "))
if((A>=B) and (B>=C)):
    print("maximum: ",A)
    print("minimum: ",C)
elif((B>=A)and(A>=C)):
     print("maximum: ",B)
     print("minimum: ",C)
elif((C>=A)and(A>=B)):
    print("maximum: ",C)
    print("minimum: ",B)
elif((A<=B)and(B<=C)):
    print("maximum: ",C)
    print("minimum:",A)
elif((B<=A)and(A<=C)):
    print("maximum: ",C)
    print("minimum: ",B)