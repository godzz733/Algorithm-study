import sys; input = sys.stdin.readline
n,m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'o':
            t = n
            for k in range(i+1,n):
                if arr[k][j] == '#':
                    t = k
                    break
            for k in range(t-1,i,-1):
                if arr[k][j] == '.':
                    arr[k][j] = 'o'
                    arr[i][j] = '.'
                    break

for i in range(n):
    print(''.join(arr[i]))