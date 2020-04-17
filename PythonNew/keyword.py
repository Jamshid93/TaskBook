# Endi bu yerda keyword arguments xaqida ,keywor argumants va positional arguments degani bir biridan farq qiladi 
# Biz positional argumentsa ni to'g'ridan to'g'ri funksiyaga bog'laymiz
# lekin keyword argumentni ko'rsatishimiz kerak funksiyani chaqirganimzida
def func_user(first_name, last_name): 
    print(f"Hi {first_name} {last_name}!") 
    print("Welcome our team !!!")

print("Start")
func_user("Jamshid",last_name="Khamzaev") # xar doim birinchi positional agrgument yoziladi undan keyin esa keyword argument yoziladi
print("Finish")
# Umuman olganda keyword argument degani shu funksiyani ichida keraklo kalit so'z orqali chaqirib olish kerakli nom orqali