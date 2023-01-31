import sys
input = sys.stdin.readline
arr= []
for _ in range(5):
    li = [*map(int,input().rstrip().split())]
    arr.append(li)

result = []
for i in arr:
    result.append(sum(i))

print(result.index(max(result))+1, max(result))
