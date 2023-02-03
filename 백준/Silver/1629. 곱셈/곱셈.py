a, b, c = map(int, input().split())
_mod = a % c

arr = [(0, _mod)]
for i in range(1, 32):
    arr.append((i, (arr[i - 1][1] ** 2) % c))
result = []
i = 31
while b>0 and i>=0:
    if b-2**i >= 0:
        result.append(arr[i])
        b -= 2**i
    else:
        i -= 1
num = 1
for i in result:
    num *= i[1]
print(num%c)