import sys; input = sys.stdin.readline
n = int(input())
def solve(n):
    if n < 250: print(4, end=' ')
    elif n < 275: print(3, end=' ')
    elif n < 300: print(2, end=' ')
    else: print(1, end=' ')
for _ in map(int,input().split()):
    solve(_)