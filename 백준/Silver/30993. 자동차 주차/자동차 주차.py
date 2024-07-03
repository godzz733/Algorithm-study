import sys; input = sys.stdin.readline
a,b,c,d = map(int, input().split())
ans = 1
for i in range(2, a+1):
    ans *= i
for i in [b,c,d]:
    for j in range(2,i+1):
        ans //= j
print(ans)