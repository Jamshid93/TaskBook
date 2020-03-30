import random

en_letters = u"abcdefghijklmnopqrstuvwxyz"
en_capital=u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = u"0123456789"

letters = en_letters + digits+en_capital

N=(input("N="))
C = random.choice(letters)
#C=(input("C="))
s=str(C)*N
print("Result:",s)
