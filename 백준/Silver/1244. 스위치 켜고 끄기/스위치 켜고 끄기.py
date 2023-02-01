import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = [*map(int,input().rstrip().split())]
m = int(input().rstrip())
for _ in range(m):
    a,b = map(int,input().rstrip().split())
    if a == 1:
        for i in range(b-1,n,b):
            if arr[i] == 0:
                arr[i]= 1
            else:
                arr[i] = 0
    else:
        if arr[b-1]==0:
            arr[b-1]=1
        else:
            arr[b-1]=0
        for i in range(1,50):
            if b-1-i<0 or b-1+i>=n:
                break
            else:
                if arr[b-1-i]==arr[b-1+i]:
                    if arr[b-1-i]==0:
                        arr[b-1-i]=1
                    else:
                        arr[b-1-i]=0
                    if arr[b-1+i]==0:
                        arr[b-1+i]=1
                    else:
                        arr[b-1+i]=0
                else:
                    break
for i in range(0,n,20):
    print(*arr[i:i+20])