n = int(input())
oper = [0,0,0,0]
arr = [*map(int,input().split())]
lst = [*map(int,input().split())]
for i in range(4):
    oper[i] += lst[i]
_min = int(1e10)
_max = -int(1e10)
def dfs(cnt,result):
    global _max, _min
    if cnt > n-1:
        if result > _max:
            _max = result
        if result < _min:
            _min = result

    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            if i == 0:
                now = result + arr[cnt]
            elif i == 1:
                now = result - arr[cnt]
            elif i == 2:
                now = result * arr[cnt]
            else:
                if result<0:
                    now = -(-result//arr[cnt])
                else:
                    now = result//arr[cnt]
            dfs(cnt+1,now)
            oper[i] += 1
dfs(1,arr[0])
print(_max)
print(_min)
