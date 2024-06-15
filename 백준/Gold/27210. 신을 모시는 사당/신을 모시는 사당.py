import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
ans = [0]
for i in arr:
    if i == 1:
        ans.append(ans[-1]+1)
    else:
        ans.append(ans[-1]-1)
ans.sort()
print(abs(ans[-1]-ans[0]))