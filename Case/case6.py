N=int(input("N= "))
L=float(input("L= "))
Length={1: (L/10),
2:(L*1000),
3:(L),
4:(L/1000),
5:(L/100)}
print(Length.get(N))
