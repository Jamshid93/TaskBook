import random
import math

r = {1 : "side a", 2 : "radius R1 of inscribed circle", \
     3 : "radius R2 of circumscribed circle", 4 : "are S"}
d = []

i = int(input("i= "))
#i = 4
print("i : ", i)
N = float(input(""))
#N = 64
print(r[i],":",N)
if i == 1:
    a = N
    R1 = a * math.sqrt(3) / 6
    R2 = R1 * 2
    S = a**2 * math.sqrt(3) / 4
elif i == 2:
    R1 = N
    a = R1 * 6 / math.sqrt(3)
    R2 = R1 * 2
    S = a**2 * math.sqrt(3) / 4
elif i == 3:
    R2 = N
    R1 = R2 / 2
    a = R1 * 6 / math.sqrt(3)
    S = a**2 * math.sqrt(3) / 4
elif i == 4:
    S = N
    a = math.sqrt(S * 4 / math.sqrt(3))
    R1 = a * math.sqrt(3) / 4
    R2 = R1 * 2

d.append(a)
d.append(R1)
d.append(R2)
d.append(S)

print()
print(":")
for i in range(0,4):
    print(r[i+1],"Elements of an equilterial tringale:",d[i])