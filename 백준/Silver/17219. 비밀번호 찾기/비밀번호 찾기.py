import sys
n,m = map(int, input().split())
dic ={}
for i in range(n):
    site,password = map(str, sys.stdin.readline().split())
    dic[site] = password
for k in range(m):
    want = str(sys.stdin.readline().rstrip())
    print(dic[want])