n, m = map(int, input().split())
a = list(input())
b = list(input())

arr = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1,n+1):
    arr[i][0] = i
for i in range(1,m+1):
    arr[0][i] = i
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1] == b[j-1]:
            arr[i][j] = arr[i-1][j-1]
        elif a[i-1] == 'i':
            if b[j-1] == 'j' or b[j-1] == 'l':
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
        elif a[i-1] == 'v':
            if b[j-1] == 'w':
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
        else:
            arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
print(arr[n][m])