import itertools
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
chi = []
home = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chi.append((i,j))
        elif arr[i][j] == 1:
            home.append((i,j))
result = int(1e9)
if m == 1:
    for j in chi:
        num = 0
        for i in home:
            num += abs(j[0] - i[0]) + abs(j[1] - i[1])
        if num < result:
            result = num
    print(result)
else:
    a= list(itertools.combinations(chi, m))
    result = int(1e9)
    for k in a:
        num = 0
        for i in home:
            _min = int(1e9)
            for j in k:
                if _min > abs(j[0] - i[0]) + abs(j[1] - i[1]):
                    _min = abs(j[0] - i[0]) + abs(j[1] - i[1])
            num += _min
        if num < result:
            result = num

    print(result)