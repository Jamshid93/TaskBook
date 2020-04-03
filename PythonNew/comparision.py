# Endi taqqoslash operatorlari ya'ni comparison operators haqida
# "==" bu ikkalasi xam teng degani 
# "!=" bu teng emas degani
# ">=" bu katta yoki teng ,"<=" bu kichik yoki teng degani

# Endi deylik bitta odamni ismi berilgan shu ismda nechta xarf bor shuni topishni va ism agar 3 ta xarfdan kam  bulsa bizga
#  ism kamida 3 ta xarfdan tashkil topishi kerak desin yoki agar shu ismdan juda ko'p xarflar bulsa bu berilgan ism eng ko'pi 
# bilan 50 ta xarfadan iborat bulsin desin , agar boshqa xolatlarda narmal ism desin
#name="1234567890101112121314151617181920212223242526272829303132343335363738394041142434546474849515023569465512sxsxsxsxsxsxsxsxsxsxsxdncadddececdcdcdcdcdcdcdcdcdcdcdcdccddcdcdcdcdcdkd"
name="Jamshid"
if len(name)<3:
    print("Ism kamida 3 ta belgidan iborat bo'lishi kerak!")
elif len(name)>50:
    print("Ism maxsimum 50 ta belgidan iborat bo'lsin")
else:
    print("Narmal ism")

    