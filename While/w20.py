N =int(input("N="))
q = N
i = 0
F = False
while q >= 1:
    i += 1
    r = q % 10
    if r == 2:
        F = True
        break
    q = int(q/10)
print(F)