import sys; input = sys.stdin.readline
t = int(input())
arr = [*map(int,input().rstrip().split())]
lst = [0]
for i in arr:
    lst.append(lst[-1]+i)
_min = 0
ans = max(arr)

for i in range(1,t+1):
    ans = max(ans,lst[i]-_min)
    _min = min(_min,lst[i])
print(ans)