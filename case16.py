import random

ten_of = {
    20 : 'twenty -',
    30 : 'thirty -',
    40 : 'forty -',
    50 : 'fifty -',
    60 : 'sixty -'
}

one_of  = {
    1 : 'one year',
    2 : 'two year',
    3 : 'three year',
    4 : 'four year',
    5 : 'five year',
    6 : 'six year',
    7 : 'seven year',
    8 : 'eight year',
    9 : 'nine year'
}

try:
    N = int(input("N= "))
    #N = 60
    r = N%10
    if r == 0:
        print("{0} year".format(ten_of[N]))
    else:
        q = int(N/10)*10
        print("{0} {1}".format(ten_of[q], one_of[r]))

except KeyError as e:
    print('Error')