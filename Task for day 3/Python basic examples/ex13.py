a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))

if a<b and a<c:
    print(a,' is smallest')
elif b<a and b<c:
    print(b,' is smallest')
elif c<a and c<b:
    print(c,' is smallest')