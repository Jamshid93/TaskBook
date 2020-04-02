# Pythonda "list" degan ma'lumot turi mavjud ko'pchilik buni "MASSIV" deb xam yuritadi
# "list" lar xam raqamlardan ya'ni 1,2,3,4,5,...... va xam so'zlarni qabul qiladi
# listlar bilan bir qancha funksiyalarni amalga oshirishimiz mumkin 
# listlar xar doim "[]" shu kabi qavs ichiga yoziladi
# listlarning bir qancha method lari bor ba'zilarini ko'rib chiqamiz
lst1=[1,2,3,4,5,6,7]
lst2=["Assalomu","alaykum","Pythonga","xush kelibsiz"]
lst3=[1,3,2,6,8,4,"Salom","Hello"]

a=lst1[0] # bu degani indexing ya'ni shu ko'rsatilgan list elementlaridagi 0 tartib raqamni ostidagi list elementini chiqar degani
print(a)

a=lst1[:4] # bu degani slaysing deyiladi ya'ni shu 4-list elementigacha olib chiqarib ber degani 
print(a)

lst1.append(100) # bu method ya'ni "append" shu ko'rsatilgan listga ya'ni list1 ga 100 raqamini qo'sh degani
print(lst1)

lst1.pop() # bu "pop" method shu ko'rsatilgan listdan oxirgi elementini olib tashlaydi
print(lst1)

a=lst1+lst2 # bu deagni concatunation ya'ni bir listni yana boshqa listga qo'shish degani
print(a)

lst1[-1]=222 # bu degani shu ko'rsatilgan listning oxirgi elementini tenglagan raqamga almashtir degani 
# ya'ni xozir bu yerda 7 ni 222 ga almashtirib qo'yayapti
print(lst1)

lst1[-1]=[123, 2, 4, 567,] # listlar ichida yana list xosil qilishimiz mumkin.
print(lst1)