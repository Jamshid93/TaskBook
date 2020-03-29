N=int(input("N="))
S=int
if(N>0):
    S=0
    for i in range(1,N+1):
        x=(1+(0.1*i))*(-1)**(i+1)
        S=S+x
    print( S)