import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [[i] for i in range(n+1)]
lst = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    if a == 0:
        if lst[b] != lst[c]:
            if len(arr[lst[b]]) < len(arr[lst[c]]):
                b,c = c,b
            arr[lst[b]] += arr[lst[c]]
            for i in arr[lst[c]]:
                lst[i] = lst[b]
    else:
        if lst[b] == lst[c]:
            print("YES")
        else:
            print("NO")