import sys; I = sys.stdin.readline
n,m = map(int,I().split())
arr = [0] + [1] * (n)
arr2 = [0] + [1] * (n)
ans = 0
for _ in range(m):
    a,b = map(int,I().split())
    arr[a] = 0
    arr2[b] = 0
c = int(I())
if not arr[c]:
    print('NOJAM')
    exit()
ans = sum(arr2) - arr2[c]
if ans == 2 and sum(arr) == 2:
    for i in range(1,n+1):
        if arr[i] and arr2[i]:
            ans = 1
            break
print(ans) if ans != 1 else print('NOJAM')