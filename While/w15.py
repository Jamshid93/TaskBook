S_start = 1000
S_end = 1100
P = float(input("P="))
coef = 1 + P/100
K = 0
S = S_start
while S < S_end:
    S *= coef
    K += 1
print("K=",K,"S=",S)
