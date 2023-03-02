lst = list(str(input()))
n = len(lst)
can = [0,0]
for c in range(20,0,-1):
    for r in range(c,0,-1):
        if c*r == n:
            if can[1] < r:
                can = [c,r]
c,r = can[0], can[1]
arr = [[0] * c for _ in range(r)]
cnt = -1
for i in range(c):
    for j in range(r):
        cnt += 1
        arr[j][i] = lst[cnt]
result = ''
for i in range(r):
    for j in range(c):
        result += arr[i][j]
print(result)
