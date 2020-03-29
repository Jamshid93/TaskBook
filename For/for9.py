A=int(input("A="))
B=int(input("B="))
sum_square=int
if(A<B):
    sum_square=0
    for i in range(A,B+1,1):
        sum_square=sum_square+pow(i,2)
    print(sum_square)