N=int(input("Write action number: "))
A=float(input("A= "))
B=float(input("B= "))
def action1():
    print("A+B=",A+B)
def action2():
    print("A-B=",A-B)
def action3():
    print("A*B=",A*B)
def action4():
    print("A/B=", A/B)
def action5():
    print("Error")

if (N==1):
    action1()
elif (N==2):
    action2()
elif (N==3):
    action3()
elif (N==4):
    action4()
else:
    action5()