import random

N = random.randrange(1, 27)
N=int(input("N="))
for i in range(N):
    print(chr(ord('a')+i), end=" ")