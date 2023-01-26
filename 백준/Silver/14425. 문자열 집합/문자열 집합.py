import sys
a, b = map(int,input().split())
dic = {}
arr= []
for _ in range(a):
    n = str(sys.stdin.readline())
    dic[n] = 0
for _ in range(b):
    m = str(sys.stdin.readline())
    arr.append(m)

for i in arr:
    if i in dic:
        dic[i] +=1

print(sum(list(dic.values())))

