import random

en_letters = u"abcdefghijklmnopqrstuvwxyz"
en_capital=u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = u"0123456789"

letters = en_letters + digits+en_capital

C = random.choice(letters)
C=input("C=")
if en_capital.find(C) != -1:
    print("Capital")
elif en_letters.find(C) != -1:
    print("single")
elif digits.find(C) != -1:
    print("Digits")
else:
    print("Not found")