# Checking data types
# print(type(10))          # Int
# print(type(3.14))        # Float
# print(type('abcde'))  # String
# print(type([8, 2, 3]))   # List
# print(type({'name':'Anvar'})) # Dictionary
# print(type({9.8, 3.14, 2.7}))    # Set
# print(type((9.8, 3.14, 2.7)))    # Tuple
# a = 5
# print(type(5))
# print(type(False))


# range([start,] stop [, step]) -> range object
# x = range(0,5,1)
# print(list(x))


# s = 0
# n = 10
# for i in range(1,n,2):
#     s += i
#     # print(i)
# print(s)

arr = [1,4,3,7,8,0,5]
n = len(arr)
print("Listning ichidagi elementlar soni: ",n)
a=0

for i in range(n):
   if (i%2!=0):
       a = a + arr[i]

print("Ko'rsatilgan listdagi toq o'rinda turgan elemnetlar yigíndisi:",a)