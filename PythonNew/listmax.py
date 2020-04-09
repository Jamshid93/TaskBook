# Deylik bizga bitta list berilgan va bu list elemnetlarining ichidan eng kattasini topish talab qilinsa 
numbers=[3,1,5,2,6,3,10,32,5,21]
max=numbers[0]
min=numbers[0]
for number in numbers:
    if number<min:
        min=number
print(f"Min number={min}")
for number in numbers:
    if number>max:
        max=number
print(f"Max number={max}")
c=min+max
print(c)