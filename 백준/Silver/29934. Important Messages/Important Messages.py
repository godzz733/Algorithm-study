import sys; input = sys.stdin.readline
_set = set()
ans = 0
for _ in range(int(input())):
    _set.add(input().rstrip())
for _ in range(int(input())):
    if input().rstrip() in _set:
        ans += 1
print(ans)