import sys; input = sys.stdin.readline
n = int(input())
m = int(input())
if n == 1 or n == 5:
    ans = 8*m + n - 1
else:
    ans = 8*(m//2)
    if m%2:
        ans += 10 - n-1
    else:
        ans += n - 1
print(ans)