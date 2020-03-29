A=float(input("A="))
N=int(input("N="))
S=int()
P=int()
if(N>0):
    S=1
    P=1
    for i in range(1,N+1):
        P=P*A*(-1)
        S=S+P
    print(S)
    