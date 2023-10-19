import sys;input = sys.stdin.readline
n = input()
ans = 0
for i in range(len(n),0,-1):
    if i % 2: continue
    for j in range(len(n)-i):
        tem = n[j:j+i]
        # print(tem)
        # print(tem[:len(tem)//2],tem[len(tem)//2:])
        if sum(map(int,tem[:len(tem)//2])) == sum(map(int,tem[len(tem)//2:])):
            # print(tem,sum(map(int,tem[:len(tem)//2])),sum(map(int,tem[len(tem)//2:])))
            ans = max(ans,i)
print(ans)