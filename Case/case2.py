K=int(input("Write mark number: "))
def action1():
    print("'bad'")
def action2():
    print("'unsatisfactory'")
def action3():
    print("'mediocre'")
def action4():
    print("'good'")
def action5():
    print("'excellent'")
def unknown_action():
    print("'Error'")

if K == 1:
    action1()
elif K == 2:
    action2()
elif K == 3:
    action3()
elif K == 4:
    action4()
elif K == 5:
    action5()
else:
    unknown_action()