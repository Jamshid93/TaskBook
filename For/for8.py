A=int(input("A="))
B=int(input("B="))
multiply=int
if(A<B):
    multiply=1
    for i in range(A,B+1,1):
        multiply=multiply*i
    print(multiply)