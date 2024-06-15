import sys; input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
def back(x,y):
    global dp
    if x == n-1 and y == n-1:
        print("HaruHaru")
        exit()
    
    for i in [(1,0), (0,1)]:
        nx, ny = x + arr[x][y] * i[0], y + arr[x][y] * i[1]
        if 0 <= nx < n and 0 <= ny < n and dp[nx][ny] == 0:
            dp[nx][ny] = 1
            back(nx, ny)
back(0,0)
print("Hing")