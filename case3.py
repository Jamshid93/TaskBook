K=int(input("Write month number: "))
def action1():
    print("'Winter'")
def action2():
    print("'Spring'")
def action3():
    print("'Summer'")
def action4():
    print("'Autumn'")
def unknown_action():
    print("'Error'")

if ((1<=K)and(K<=2)or(K==12)):
    action1()
elif ((3<=K)and(K<=5)):
    action2()
elif ((6<=K)and(K<=8)):
    action3()
elif ((9<=K)and(K<=11)):
    action4()
else:
    unknown_action()