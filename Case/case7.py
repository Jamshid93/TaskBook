N=int(input("N= "))
M=float(input("M= "))
Weight={1: (M),
2:(M/1000000),
3:(M/1000),
4:(M*1000),
5:(M*100)}
print(Weight.get(N))
