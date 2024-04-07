import sys; input = sys.stdin.readline
n,m = map(int,input().split())
ans = 0
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    if a >= b: ans += 1
    else:
        arr.append((a,b))
arr.sort(reverse=True)
# print(arr)
while arr:
    ans += 1
    arr.pop()
    tem = m-1
    while arr and tem > 0:
        a,b = arr.pop()
        if tem < a:
            if not arr:
                ans += 1
                print(ans)
                exit()
            c,d = arr.pop()
            arr.append((c-tem,d))
            arr.append((a,b))
            break
        tem -= a
print(ans)