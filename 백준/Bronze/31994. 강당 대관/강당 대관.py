import sys; input = sys.stdin.readline

arr = []
for _ in range(7):
    a,b = map(str,input().rstrip().split())
    arr.append((a,int(b)))
arr.sort(key=lambda x: x[1], reverse=True)
print(arr[0][0])