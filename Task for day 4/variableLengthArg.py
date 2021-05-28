def add(*a):
    sum = 0

    for n in a:
        sum = sum + n
    print('sum: ',sum)

def add2(**b):
    print('output using variable length with keyword')
    for i,j in b.items():
        print(i, j)

add(10,10)
add(20,30,40)

add2(name='Het', surname='Vaghasia')