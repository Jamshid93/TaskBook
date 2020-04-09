# Eni 2D listlar xaqida 2 D list degani bitta list ichida yana bitta list bor degani
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#matrix[0][1]=20 # bu yerda [0] deyilgani birinchi listning ichidagi birnchi ya'ni [1,2,3] list degani [1]esa shu ikkinchi listning
# 1-chi tartib raqam ostidagi elementi degani ya'ni bu 2 ga teng bizda
#print(matrix[0][1])

# Endi bizga shu yuqoridagi 2D listning xamma elementlarini chiqarish kerak bo'lsa
for row in matrix: # bu yerda row birinchi listning elemetlari ya'ni [1,2,3], [4,5,], [7,8,9]
    for item in row: # bu yerda item birinchi listning ichidagi ikkinchi list elemetlari ya'ni 1,2,3,4,5,6,7,8,9 
        print(item)