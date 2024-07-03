import sys; input = sys.stdin.readline
_,m = map(int, input().split())
for i in sorted(list(map(int, input().split()))):
    if i <= m:m += 1
print(m)