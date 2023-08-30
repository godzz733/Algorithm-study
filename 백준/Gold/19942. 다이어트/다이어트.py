ans = []
n = int(input())
food = list(map(int,input().split()))
arr = []
for i in range(1,n+1):
    arr.append(list(map(int,input().split())))
answer = [[0,0,0,0],987654321,[]]
def back(idx,cnt,ans):
    global answer
    if idx == n:
        for i in range(4):
            if food[i] > answer[0][i]:
                return
        if cnt < answer[1]:
            answer[1] = cnt
            answer[2] = ans[:]
        elif cnt == answer[1]:
            if ans < answer[2]:
                answer[2] = ans[:]
        return
    for j in range(4):
        answer[0][j] += arr[idx][j]
    
    back(idx+1,cnt+arr[idx][4],ans+[idx+1])
    for j in range(4):
        answer[0][j] -= arr[idx][j]
    back(idx+1,cnt,ans)
back(0,0,[])
if answer[1] == 987654321:
    print(-1)
else:
    print(answer[1])
    print(*answer[2])