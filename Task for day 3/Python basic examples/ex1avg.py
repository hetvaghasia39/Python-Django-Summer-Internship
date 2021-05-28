# average of 5 input numbers

print('enter any 5 numbers')
l1 = []
count = 0
sum = 0
for i in range(5):
    inp = int(input('Enter number: '))
    l1.append(inp)
    sum = sum + l1[i]
    count += 1
avg = sum/count
print('average: ',avg)