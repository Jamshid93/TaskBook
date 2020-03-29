import math

r = {1 : "radius R", 2 : "diametr D", 3 : "length L", 4 : "are circle S"}
c = []

i =int(input("i= "))
print(i)
N = float(input(""))
print(r[i],":",N)
if i == 1:
    R = N
    c.append(R)
    c.append(2 * R)
    c.append(2 * math.pi * R)
    c.append(math.pi * R**2)
elif i == 2:
    D = N
    R = D / 2
    c.append(R)
    c.append(D)
    c.append(math.pi * D)
    c.append(math.pi * R**2)
elif i == 3:
    L = N
    R = L / 2 / math.pi
    c.append(R)
    c.append(2 * R)
    c.append(L)
    c.append(math.pi * R**2)
elif i == 4:
    S = N
    R = math.sqrt(S / math.pi)
    c.append(R)
    c.append(2 * R)
    c.append(2 * math.pi * R)
    c.append(S)

print()
print("Elements of a circle:")
for i in range(0,4):
    print(r[i+1],":",c[i])