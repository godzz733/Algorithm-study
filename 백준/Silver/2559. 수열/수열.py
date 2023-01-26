import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [*map(int,input().split())]
start = 0
end = m
ori = 0
for i in range(start,end):
    ori += arr[i]
maxi = ori
if m==1:
    print(max(arr))
elif m==n:
    print(sum(arr))
else:
    while 1:      
        ori -= arr[start]
        ori += arr[end]
        if ori>maxi:
            maxi = ori
        start+=1
        end+=1
        if end==n:
            break

    print(maxi)
        
    

        