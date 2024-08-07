import sys; input = sys.stdin.readline

n = int(input())
t = list(input().rstrip())
m = int(input())
for i in range(n):
    if t[i] == "1":
        t = ''.join(reversed(t[i:]))
        break
else:
    print("YES")
    exit()
if m > len(t):
    print("NO")
    exit()

for i in range(m):
    if t[i] == '1':
        print("NO")
        break
else:
    print("YES")