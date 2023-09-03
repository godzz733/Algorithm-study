a,b = map(str,input().split())
ans = 100
for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if b[i+j] != a[j]:cnt+= 1
    ans = min(ans,cnt)
print(ans) 