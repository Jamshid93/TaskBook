N=int(input("N="))
Factorial=int()
if(N>0):
    Factorial=1
    for i in range(1,N+1):
        Factorial=Factorial*i
    print(Factorial)
    