n = int(input())
idx = 64
ans = 0
while n:
    ans += n//idx
    n %= idx
    idx >>= 1
print(ans)