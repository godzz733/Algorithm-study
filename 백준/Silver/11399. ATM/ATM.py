n = int(input())
arr = [*map(int,input().split())]
arr.sort()
num = 0
if n ==0:
    num = arr[0]
else:
    for i in range(1,n+1):
        num+= sum(arr[:i])

print(num)

