K=int(input("Write month number: "))
def action1():
    print("31")
def action2():
    print("28")
def action3():
    print("30")
def unknown_action():
    print("'Error'")

if ((K==1)or(K==3)or(K==5)or(K==7)or(K==8)or(K==10)or(K==12)):
    action1()
elif (K==2):
    action2()
elif ((K==4)or(K==6)or(K==9)or(K==11)):
    action3()
else:
    unknown_action()