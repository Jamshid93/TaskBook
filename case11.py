C=str(input("C= "))
N1=int(input("N1= "))
N2=int(input("N2= "))
CCC={
    'N':[(1=='W'),(2=='N'),(-1=='E')],
    'E':[(1=='N'),(2=='E'),(-1=='S')],
    'S':[(1=='E'),(2=='S'),(-1=='W')],
    'W':[(1=='S'),(2=='W'),(-1=='N')]
}
if(C=='N')and(C=='E')and(C=='S')and(C=='W'):
    print(CCC.get(C))