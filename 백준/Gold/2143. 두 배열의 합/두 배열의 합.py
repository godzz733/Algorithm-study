import sys; input = sys.stdin.readline
t = int(input())
n = int(input())
ans = 0
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
t1 = [0]
t2 = [0]
ans1 = []
ans2 = []
for i in range(n):
    t1.append(t1[-1] + arr1[i])
for i in range(m):
    t2.append(t2[-1] + arr2[i])
for i in range(1,n+1):
    for j in range(i):
        ans1.append(t1[i]-t1[j])
for i in range(1,m+1):
    for j in range(i):
        ans2.append(t2[i]-t2[j])
dic1, dic2 = {}, {}
for i in ans1:
    dic1[i] = dic1.get(i,0) + 1
for i in ans2:
    dic2[i] = dic2.get(i,0) + 1
for x,y in dic1.items():
    if x == t:
        ans += dic2.get(0,0) * y
    else:
        ans += dic2.get(t-x,0) * y
print(ans)