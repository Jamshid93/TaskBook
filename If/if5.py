A1=int(input("A1= "))
A2=int(input("A2= "))
A3=int(input("A3= "))
N=int(0)
B=int(0)
if (A1>0):
    N=N+1
if (A2>0):
    N=N+1
if (A3>0):
    N=N+1
if  (A1<0):
    B=B+1
if (A2<0):
    B=B+1
if (A3<0):
    B=B+1
print("positive ",N)
print("negative ",B)