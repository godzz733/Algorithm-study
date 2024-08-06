import sys; input = sys.stdin.readline

n = int(input())
arr = []
dic = set()
for _ in range(n):
    lst = list(input().rstrip().split())
    for i in range(len(lst)):
        if lst[i][0].upper() not in dic:
            dic.add(lst[i][0].upper())
            lst[i] = "[" + lst[i][0] + "]" + ''.join(lst[i][1:])
            break
    else:
        for i in range(len(lst)):
            key = 0
            for j in range(len(lst[i])):
                if lst[i][j].upper() not in dic:
                    dic.add(lst[i][j].upper())
                    lst[i] = ''.join(lst[i][:j]) + "[" + lst[i][j] + "]" + ''.join(lst[i][j+1:])
                    key = 1
                    break
            if key:
                break
    ans = ""
    for i in lst:
        ans += i + " "
    arr.append(ans.rstrip())
for i in arr:
    print(i)