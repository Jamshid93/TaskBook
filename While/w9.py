N=int(input("N="))
K=1
if N>1:
    while (3**K)<=N:
        K=K+1
print("K=",K)