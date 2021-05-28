a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))

if a < b:
    if b < c:
        print(c,' is greatest')
    else:
        print(b,' is greatest')
elif b < c:
    if c < a:
        print(a,' is greatest')
    else:
        print(c,' is greatest')