# range function example
for i in range(10):
    print('value is ',i)

for i in range(1,5):
    print('value is ',i)

for i in range(1,10,2):
    print('value is ',i)

# collection len() range() fusion example
l1 = [21, 32, 3, 64]
print(l1)

for i in range(len(l1)):
    print('value is ',i)