N = int(input("N="))
K = 1
S = 1
while S <= N:
    K += 1
    S += K
S -= K
K -= 1
print("K=",K,"S=",S)