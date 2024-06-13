import sys; input = sys.stdin.readline
n,m = map(int,input().split())

for _ in range(m):
    if n & 1:
        n = 2*n ^ 6
    else:
        n = (n//2) ^ 6
print(n)