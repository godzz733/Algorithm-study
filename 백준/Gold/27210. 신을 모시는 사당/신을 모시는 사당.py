import sys; input = sys.stdin.readline
n = int(input())
arr = [1 if i == 1 else -1 for i in list(map(int,input().split()))]
ans = [0]
for i in arr:
    ans.append(ans[-1]+i)
print(abs(max(ans)-min(ans)))