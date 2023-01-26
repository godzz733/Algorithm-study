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
    
    if result<b: #최소값을 구해야하기때문에 결과값이 작을 때 mid에 1을 추가
        start = mid+1
    else: #최소값을 구할 때 까지 mid-1을 함
        end = mid-1
        num = mid

print(num)
        
