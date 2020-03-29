import math
A=int(input("A= "))
B=int(input("B= "))
C=int(input("C= "))
Number_squares=int(int(A/C)*int(B/C))
Unused_part=int(int(A*B)-int(Number_squares*pow(C,2)))
print(Number_squares)
print(Unused_part)