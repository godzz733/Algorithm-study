import sys
input = sys.stdin.readline
a,b = map(int,input().split())
arr= [*map(int, input().split())]
start = 0
end = min(arr)*b
num = 0
while start<=end:
    result = 0
    mid = (start+end)//2
    for i in arr:
        result+=mid//i
    
    if result<b:
        start = mid+1
    else:
        end = mid-1
        num = mid

print(num)
        
