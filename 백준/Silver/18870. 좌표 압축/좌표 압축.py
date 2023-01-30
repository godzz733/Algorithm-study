import sys
input = sys.stdin.readline
n = int(input())
dic = {}
arr = [*map(int,input().rstrip().split())]
count = 0
sor_arr = sorted(list(set(arr)))
for i in sor_arr:
    dic[i] = count
    count+=1
for i in arr:
    print(dic[i],end=' ')
