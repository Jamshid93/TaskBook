# Endi bunda funksiyaning parametrlarini ko'rib chiqamiz
def func_user(first_name, last_name): # bu degani bu yerga qavsni ichiga kerakli argumentni yozamiz xoxlagan narsamizni
    print(f"Hi {first_name} {last_name}!") # agar bizga ism va familyasini chiqarish kerak bo'lsa
    print("Welcome our team !!!")

print("Start")
func_user("Jamshid","Khamzaev") # bu yerda shu funksiyaga kiritlgan  ya'ni positional argumentga shu so'zni ta'minlab qoýayampmiz.
func_user("Bobur", "Karshibaev")
print("Finish")