A=int(input("A= "))
hundred=int(A/100)
tens=int(A/10%10)
ones=int(A%10)
print(hundred*10+tens+ones*100)