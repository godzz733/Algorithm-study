n, m, l = map(int, input().split())
arr = [1] + [0] * (n-1)
baller = cnt = 0
while 1:
    if arr[baller] == m:
        break
    cnt += 1
    if arr[baller] % 2:
        arr[(baller+l)%n] += 1
        baller = (baller+l) % n
    else:
        arr[-1*(abs((baller-l))%n)] += 1
        baller = -1*(abs((baller-l))%n)
print(cnt)