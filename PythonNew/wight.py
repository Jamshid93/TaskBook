# Bizga odamni boýiga qarab kg ni chiqarib berish kerak bo'lsin yoki uni teskarisi kg qarab boýini
weight=int(input("Ogírligi:"))
unit=input("Boýi(sm) yoki o'g'rilig(kg):")
if unit.upper()=="L":
    converted=weight*0.45
    print(f"Siz ogírligingiz {converted}  kg")
else:
    converted=weight/0.45
    print(f"Sizning boýingiz {converted} sm")