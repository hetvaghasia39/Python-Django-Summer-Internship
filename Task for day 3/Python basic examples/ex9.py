a = int(input('enter number: '))

if a < 100:
    if a % 2 == 0:
        print(a,' is even and less than hundred')
    else:
        print(a,' is odd and less than hundred')
elif a==100:
    print(a,' is equal to hundred')
else:
    print(a,' is greater than hundred')