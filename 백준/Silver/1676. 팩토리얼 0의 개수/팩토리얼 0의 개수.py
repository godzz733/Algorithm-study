n = int(input())
result = 0
for i in range(4,n+1):
    if not i%5:
        while not i%5:
            result += 1
            i /=5
print(result)