import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
lst = [input().rstrip() for _ in range(n)]
arr = {}
st = 0
for i in range(n-1):
    a,b = map(int, input().split())
    if i == n-2:
        st = a
    if a not in arr:
        arr[a] = [b]
    else:
        if b in arr:
            arr[a].append(b)
        else:
            arr[a].append(b)
print(lst[st-1],end='')
def ans(x):
    for i in arr[x]:
        print(lst[i-1],end='')
        if i in arr:
            ans(i)
ans(st)