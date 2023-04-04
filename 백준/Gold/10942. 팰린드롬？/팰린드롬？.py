import sys
input = sys.stdin.readline
n = int(input())
arr = [*map(int,input().split())]
dp = [[False] * n for _ in range(n)]

for i in range(n):
    for start in range(n):
        end = start + i
        if end>=n: #길이를 넘으면 중지
            break
        if i ==0: #길이가 1 일때는 무조건 팰린드롬
            dp[start][end] = True
            continue
        if i == 1: #길이가 2이면 시작과 끝이 같으면 팰린드롬
            if arr[start] == arr[end]:
                dp[start][end] = True
            continue
        if arr[start] == arr[end] and dp[start+1][end-1]: # 만약 시작과 끝이 같고 그 안이 팰린드롬이면 팰린드롬롬            dp[start][end] = True
            dp[start][end] = True
m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    if dp[a-1][b-1]:
        print(1)
    else:
        print(0)
