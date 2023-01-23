import sys
a,b = map(int, input().split())
lis_arr = {}

result = []
for _ in range(a):
    lis = str(sys.stdin.readline().rstrip())
    lis_arr[lis]=1
for _ in range(b):
    see = str(sys.stdin.readline().rstrip())
    if see in lis_arr:
        result.append(see)

result.sort()
print(len(result))
for k in result:
    print(k)
