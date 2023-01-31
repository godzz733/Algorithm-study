import sys
input = sys.stdin.readline
arr = list(str(input()))
n = int(input())
for _ in range(n):
    a,b,c = map(str, input().split())
    num = 0
    result = 0
    for i in range(int(b),int(c)+1):
        if a == arr[i]:
            result +=1
    
    print(result)
    