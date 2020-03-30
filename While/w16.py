Daily = 10
Total = 200
P =float(input("P="))
coef = 1 + P/100
K = 1
S = Daily
while S < Total:
    Daily *= coef
    S += Daily
    K += 1
print("K=",K,"S=",S)