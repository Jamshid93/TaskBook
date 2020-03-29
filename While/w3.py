N=float(input("N="))
K=float(input("K="))
R=N-K
N=1
while R>=K:
    R=R-K
    N=N+1
print("Quotient: ",N)
print("Remainder: ",R)


