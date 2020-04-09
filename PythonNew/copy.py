# Endi bu deylik listimizda bir xildagi elementlar takrorlangan bizga shuni takrorlangan elementlarni olib tashlash kerak bulsin.
numbers=[2,2,3,1,1,5,5,4]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)