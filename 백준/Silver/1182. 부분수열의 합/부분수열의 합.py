n, s = map(int, input().split())
arr = [*map(int, input().split())]
cnt = 0
result = []
for i in range(1<<n):
    li = []
    for j in range(n):
        if i&(1<<j):
            li.append(arr[j])
    result.append(li)
for i in result:
    if i and sum(i) == s:
        cnt += 1
print(cnt)