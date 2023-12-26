import sys;input = sys.stdin.readline
for k in range(1,int(input())+1):
    n = int(input())
    arr = [*map(int,input().split())]
    ans = []
    for i in arr:
        if i * 4 // 3 in arr:
            ans.append(i)
            arr.remove(i * 4 // 3)
    print(f"Case #{k}:",*ans)