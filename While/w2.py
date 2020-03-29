A=float(input("A="))
B=float(input("B="))
R=A-B
N=1
while R>=B:
    R=R-B
    N=N+1
print("Amount of sgments B: ",N)
