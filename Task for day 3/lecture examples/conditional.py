# examples for conditional statements

#if statement
a = int(input('enter num1: '))
b = int(input('enter num2: '))
if a < b:
    print(b,' is greater than ',a)

if b < a:
    print(a,' is greater than ',b)


# if else example
c = int(input('enter num3: '))
d = int(input('enter num4: '))
if c < d:
    print(d,' is greater than ',c)

else:
    print(c,' is greater than ',d)

# elif example
e = int(input('enter num5: '))
f = int(input('enter num6: '))
if e == f:
    print(e,' and ',f,' are equal')
elif e < f:
    print(f,' greater than ',e)
else:
    print(e,' greater than ',f)