n = int(input())
arr = [*map(int, input().split())]
result = []
for i in range(n):
    if not arr:
        result.append(i)
    else:
        result.insert(len(result)-arr[i],i+1)
print(*result)