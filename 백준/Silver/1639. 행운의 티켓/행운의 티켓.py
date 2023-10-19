import sys;input = sys.stdin.readline
n = input()
for i in range(len(n),0,-1):
    if i % 2: continue
    for j in range(len(n)-i):
        tem = n[j:j+i]
        if sum(map(int,tem[:len(tem)//2])) == sum(map(int,tem[len(tem)//2:])):
            print(i)
            sys.exit()
print(0)