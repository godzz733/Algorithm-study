import sys; input = sys.stdin.readline
n = int(input())
arr = [*map(int,input().rstrip().split())]
l = [0]
r = [0]
for i in map(int,input().rstrip().split()):
    l.append(l[-1]+i)
for i in map(int,input().rstrip().split()):
    r.append(r[-1]+i)
ans = [0,int(1e12)]
for i in range(n):
    t = l[i]+ r[n-1] - r[i] + arr[i]
    if ans[1] > t:
        ans[1] = t
        ans[0] = i + 1

print(*ans)