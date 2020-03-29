N=int(input("N="))
Factorial=float()
F2=float()
if(N>0):
    Factorial=0
    F2=1
    for i in range(1,N+1):
        F2=F2*i
        Factorial=Factorial+F2
    print(Factorial)
    