import sys; input = sys.stdin.readline
n = input().rstrip()
n = int(n.split(":")[0]) * 60 + int(n.split(":")[1])
if n == 30:
    print(1)
    exit()
ans = 1

arr = [600,60,30,10]
for i in arr:
    if i == 30 and n//i:
        ans -= 1
    ans += n // i
    n %= i
print(ans)