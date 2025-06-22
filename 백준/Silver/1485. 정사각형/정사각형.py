import sys; input = sys.stdin.readline
for _ in range(int(input())):
    arr = list(list(map(int, input().split())) for _ in range(4))
    t = []
    for i in range(4):
        for j in range(i+1,4):
            t.append(abs(arr[i][0] - arr[j][0])**2 + abs(arr[i][1] - arr[j][1])**2)
            t.sort()
    if t.count(t[0]) == 4 and t.count(t[-1]) == 2:
        if t[0] + t[1] == t[-1]:
            print(1)
            continue
    print(0)