

print ('Program for reading numbers from right to left')
n = int(input('enter the number n -> '))
print('Number from right to left:', end = ' ')
k = 0
n2 = n
while n2 != 0:
    n2 //= 10
    k += 1

n3 = 0
for i in range(k - 1, -1, -1):
    a = n % 10
    n3 = n3 + a * 10 ** i
    n //= 10
print(n3)

print('+New commit')