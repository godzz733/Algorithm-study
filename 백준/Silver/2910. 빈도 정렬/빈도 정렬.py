import sys; input = sys.stdin.readline
n,m = map(int,input().split())
dic = {}
arr = list(map(int,input().split()))
for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]] = [1,i]
    else:
        dic[arr[i]][0] += 1

for x,y in sorted(dic.items(),key=lambda x:(-x[1][0],x[1][1])):
    for _ in range(y[0]):
        print(x,end=' ')