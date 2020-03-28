import math
A=float(input("A= "))
B=float(input("B= "))
C=float(input("C= "))
D=(pow(B,2))-4*A*C
smaller_root=(-B-math.sqrt(D))/(2*A)
larger_root=(-B+math.sqrt(D))/(2*A)
print("x1= ",smaller_root)
print("x2= ",larger_root)