import sys; input = sys.stdin.readline
for _ in range(int(input())):
    t = input().strip()
    if len(t) < 6 or len(t) > 9:
        print("no")
    else:
        print("yes")