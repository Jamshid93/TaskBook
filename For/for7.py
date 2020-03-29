A=int(input("A="))
B=int(input("B="))
sum=int
if(A<B):
    sum=0
    for i in range(A,B+1,1):
        sum=sum+i
    print(sum)