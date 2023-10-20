import sys;input = sys.stdin.readline
n = input().rstrip()
a = n[0]
q = [0,0]
for i in range(1,len(n)):
    if n[i] != a:
        q[int(a)] += 1
        a = n[i]
q[int(a)] += 1
print(min(q))