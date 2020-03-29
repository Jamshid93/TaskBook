N=int(input("N="))
sum_multiply=int
if(N>0):
    sum_multiply=1
    for i in range(1,N+1):
        sum_multiply= sum_multiply*(1+(0.1*i))
    print( sum_multiply)