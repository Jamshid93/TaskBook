N =int(input("N="))
q = N
while q >= 1:
    r = q % 10
    q = int(q/10)
    print(r)