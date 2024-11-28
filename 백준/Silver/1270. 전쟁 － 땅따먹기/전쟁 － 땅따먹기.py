import sys; input = sys.stdin.readline
for _ in range(int(input())):
    arr = [*map(int,input().rstrip().split())]
    dic = {}
    for i in arr[1:]:
        dic[i] = dic.get(i,0) + 1
    ans = [(i,dic[i]) for i in dic]
    ans.sort(key=lambda x:(-x[1],x[0]))
    
    if ans[0][1] > arr[0]/2:
        print(ans[0][0])
    else:
        print("SYJKGW")