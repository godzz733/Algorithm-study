import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    arr1 = [*map(int,input().split())]
    arr1.sort()
    arr2 = [*map(int,input().split())]
    arr2.sort()
    i = 0
    result = 0
    for i in range(n):
        j = 0
        count = 0
        while j<m:
            if arr1[i]>arr2[j]:
                count +=1
                j+=1
            else:
                break
        result += count
    print(result)

