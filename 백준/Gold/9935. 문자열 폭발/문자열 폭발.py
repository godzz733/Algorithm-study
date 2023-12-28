import sys;input = sys.stdin.readline
a,b = list(reversed(input().rstrip())),list(reversed(input().rstrip()))
idx1,idx2 = 0,len(b)
ans = []
while a:
    if a[-1] != b[idx2-1]:
        if idx2 != len(b) and a[-1] == b[len(b)-1]:
            idx2 = len(b) - 1
        else:
            idx2 = len(b)
        ans.append(a.pop())
    else:
        ans.append(a.pop())
        idx2 -= 1
    if idx2 == 0:
        for _ in range(len(b)):
            ans.pop()
        idx2 = len(b)
        for _ in range(len(b) if len(ans) >= len(b) else len(ans)):
            a.append(ans.pop())
print(''.join(ans) if ans else 'FRULA')