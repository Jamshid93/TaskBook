N=int(input("N="))
K=0
F=1
if N>1:
    while F<N:
        F=F*3
        K=K+1
K=K-1
print("K=",K)


