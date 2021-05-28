# factorial of input number
n = int(input('enter number: '))

def fact(n):
    if n == 1:
        return 1
    f = n * fact(n - 1)
    return f

ans = fact(n)
print('Factorial of ',n,' is ',ans)

