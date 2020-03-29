action=int(input("Write week number: "))
def action1():
    print("'Monday'")
def action2():
    print("'Tuesday'")
def action3():
    print("'Wednsday'")
def action4():
    print("'Thursday'")
def action5():
    print("'Friday'")
def action6():
    print("'Saturday'")
def action7():
    print("'Sunday'")
def unknown_action():
    print("'Unknown week day'")

if action == 1:
    action1()
elif action == 2:
    action2()
elif action == 3:
    action3()
elif action == 4:
    action4()
elif action == 5:
    action5()
elif action == 6:
    action6()
elif action == 7:
    action7()
else:
    unknown_action()