# Endi yana bitta mashina bilan bog'liq oýin yasaymiz kichginagina oýin
# Deyli agar biz "start" deb yozsak bizga "Car started" deb chiqarsin
# Deylik agar biz "stop" deb kamanda bersak "Car stopped" deb chiqarsin
# Deylik "qiut" deb kamanda bersak oýin to'xtatilsin
# Agar biz oýin qoidalarini bilsh umuman yordam uchun "help" deb kamanda bersak bizga
# start= to start the car , stop=to stop the card, quit=to quit  ( xech narsa, oýin to'xtaydi) ,deb chiqrishi kerak
command=""
started=False # bu degani agar shu yolgónga teng degani
while True: # bu degani shu xolat rost bo'landa takrorlayver degani
    command=input(">").lower() # bu degani shu kirgizish uchun buyruqni va lower metodi bilan agar katta xarfda yozsa xam kichika 
                                  #o'tkaz degani
    if command == "start":
        if started:
            print("Car is already started... ")
        else:
            started=True
            print("Car started...")
    elif command == "stop":
        if not started: # bu degani agar mashina yurgani yuq bo'lsa degani 
            print("Car is already stopped...")
        else:
            started=False
            print("Car stopped...")
    elif command == "help":
        print(""" 
start - to start the car
stop - to stop the car
quit - to quit the car
        """) # bu yerdagi """ 3 ta qilganimiz xar birini yangi qatordan chiqar degani
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that ! :(")

