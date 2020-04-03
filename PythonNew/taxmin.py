# Endi shu while operatoridan foydalanim taxmin qilish oýinini yasaymiz
# Biz bitta luboy sonni yashiramiz agar oýin ishtirokchisi 3 marta imkoniyat beriladi bu yashiringan nomerni topish uchun
# Yashiringan sonni topsa yutadi agar 3 marta urunishda xam topolmasa yutqazadi
guess_count=0# bu degani hisoblashni 0 dan boshla degani
guess_limit=3 # bu degani taxmin qilishni 3 marta amalga oshirish mumkin degani
secret_number=8 # bu biz yashirib qoýgan son shuni topish kerak bo'ladi
while guess_count<guess_limit:
    guess=int(input("Guess:")) # bu degani shu qaysi sonni topish uchun kiritish
    guess_count=guess_count+1 # bu degani 1 tadan oshirib bor imkoniyatni degani
    if guess==secret_number:
        print("You won ! :) ")
        break # bu degani shu shart bajarilsa boshqa takrorlama shu yerida to'xta degani
else:
    print("Sorry you field!  :(")