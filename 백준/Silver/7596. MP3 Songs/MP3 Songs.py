import sys; input = sys.stdin.readline
idx = 0
while 1:
    idx += 1
    n = int(input())
    if not n:
        break
    arr = [input().rstrip() for _ in range(n)]
    print(idx)
    for i in sorted(arr):
        print(i)