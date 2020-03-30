A = float(input("A="))
K = 1
S = 1.0
while (S+1/(K+1) )< A:
    K += 1
    x = 1/K
    S =S+x
print("K =",K, "Sum=",S)