_suit = {
    1 : 'spades',
    2 : 'clubs',
    3 : 'diamons',
    4 : 'heards'
}

_value  = {
    6 : 'six of',
    7 : 'seven of ',
    8 : 'eight of',
    9 : 'nine of',
    10 : 'ten of',
    11 : 'Jack of',
    12 : 'Queen of',
    13 : 'King of',
    14 : 'Ace of'
}

try:
    N =int(input("Card value: ")) 
    M = int(input("Suit card: "))
    print( _value[N], _suit[M])

except KeyError as e:
    print('Error')