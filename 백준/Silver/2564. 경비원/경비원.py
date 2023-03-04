n, m = map(int,input().split())
k = int(input())
arr = []
result = 0
for _ in range(k):
    a, b = map(int, input().split())
    arr.append((a,b))
x, y = map(int, input().split())
if x == 1:
    for a, b in arr:
        if a == 1:
            result += abs(y-b)
        elif a == 2:
            result += min(m+n-y+n-b,m+y+b)
        elif a == 3:
            result += b+y
        else:
            result += b+n-y
elif x == 2:
    for a, b in arr:
        if a==2:
            result += abs(y-b)
        elif a == 1:
            result += min(m+n-y+n-b,m+y+b)
        elif a == 3:
            result += m-b+y
        else:
            result += n-y+m-b
elif x == 3:
    for a, b in arr:
        if a==3:
            result += abs(y-b)
        elif a == 1:
            result += y+b
        elif a == 2:
            result += n-b+y
        else:
            result += min(y+n+b,m-y+n+m-b)

elif x == 4:
    for a, b in arr:
        if a==4:
            result += abs(y-b)
        elif a == 1:
            result += n-b+y
        elif a == 3:
            result += min(n+b+y,n+m-y+m-b)
        else:
            result += m-y+n-b
print(result)

