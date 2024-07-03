import sys; input = sys.stdin.readline
dic = {}
for _ in range(int(input())):
    t = list(input().rstrip().split("="))
    dic[t[0].strip()] = t[1].strip()
for _ in range(int(input())):
    _ = input()
    for i in list(map(str,input().rstrip().split())):
        print(dic[i],end=" ")
    print()