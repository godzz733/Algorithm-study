import sys; input = sys.stdin.readline
for tc in range(int(input())):
    n = int(input())
    arr = [0] * 50
    for _ in range(n):
        for i in list(map(int, input().split())):
            arr[i] += 1
    tarr = [(arr[i],i) for i in range(1,50)]
    tarr.sort(key=lambda x: (-x[0], x[1]))
    ans = []
    for i in range(5):
        ans.append(tarr[i][1])
    if 7 in ans:
        ans.append(tarr[5][1])
    else:
        if arr[7] == arr[tarr[5][1]]:
            ans.append(7)
        else:
            ans.append(tarr[5][1])
    print(*sorted(ans))