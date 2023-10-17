import sys;input = sys.stdin.readline
n = int(input())
st = 0
fi = 1
cnt = 1
ans = 1
while st<fi and fi < n:
    if cnt > n:
        cnt -= st
        st += 1
    elif cnt < n:
        fi += 1
        cnt += fi
    else:
        ans += 1
        cnt -= st
        st += 1
        fi += 1
        cnt += fi
print(ans)