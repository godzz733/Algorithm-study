import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = []
for i in range(n):
    a = [*map(int, input().rstrip().split())]
    arr.append(a)
for k in range(n):
    for a in range(n):
        for b in range(n):            
            if arr[a][k] + arr[k][b] == 2:
                arr[a][b] = 1
for i in range(n):
    print(' '.join(map(str , arr[i])))
