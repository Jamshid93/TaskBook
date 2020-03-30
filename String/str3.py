import random
C=random.randrange(32,126)
c=(input("C="))
c=chr(C)

C1=ord(c)-1
C2=ord(c)+1
print("Pereceds C: ",C1)
print("Next C:",C2)