import sys;input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
lst = []
for i in range(n):
    lst.append((arr[i], i))
lst.sort()
for i in range(n):
    x,y = lst[i]
    arr[y] = i
print(*arr)