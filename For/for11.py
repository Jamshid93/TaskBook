N=int(input("N="))
sum=int
if(N>0):
    sum=0
    for i in range(N,2*N+1):
        x=i**2
        sum=sum+x
    print(sum)