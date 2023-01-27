import sys
input = sys.stdin.readline
t = int(input())

start = 0
end = t
result = 0
while start<=end:
    mid = (start+end)//2
    if mid**2<t:
        start = mid + 1
    else:
        end = mid -1
        result = mid
print(result)

