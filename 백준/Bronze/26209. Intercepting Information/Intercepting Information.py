import sys; input = sys.stdin.readline
for i in map(int,input().rstrip().split()):
    if i & 1<<3:
        print("F")
        break
else:
    print("S")