Year=int(input("Year: "))
if (((Year%100)==0) or((Year%4)==0)):
    print("This year is ",366," days")
elif(((Year%100)==0) or ((Year%400)!=0)):
    print("This year is ",365," days")