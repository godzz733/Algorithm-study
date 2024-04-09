import sys; input = sys.stdin.readline
n, l, r = map(int, input().split())
arr = [[],[],[]]
ans = 9000000001
for _ in range(n):
    a,b = map(int, input().split())
    if a <= l and b >= r:
        print(0)
        exit()
    if b < l or a > r:
        continue
    if a <= l:
        arr[0].append((a,b))
    elif b >= r:
        arr[2].append((a,b))
    else:
        arr[1].append((a,b))
if not arr[0] or not arr[2]:
    print(-1)
    exit()
arr[0].sort(key = lambda x : x[1])
arr[2].sort(key= lambda x : x[0])

def bisect1(x,y):
    global ans
    st = 0
    fi = len(arr[2]) - 1
    res = 0
    while st <= fi:
        mid = (st + fi) // 2
        if arr[2][mid][0] > y:
            fi = mid - 1
        else:
            st = mid + 1
            res = arr[2][mid][0]
    if not res:
        return
    ans = min(ans, abs(y - res))
def bisect2(x,y):
    global ans
    st = 0
    fi = len(arr[0]) - 1
    res = 0
    tem = 0
    while st <= fi:
        mid = (st + fi) // 2
        if arr[0][mid][1] < x:
            st = mid + 1
        else:
            fi = mid - 1
            res = arr[0][mid][1]
    if not res:
        return
    tem += abs(res - x)
    st = 0
    fi = len(arr[2]) - 1
    res = 0
    while st <= fi:
        mid = (st + fi) // 2
        if arr[2][mid][0] > y:
            fi = mid - 1
        else:
            st = mid + 1
            res = arr[2][mid][0]
    if not res:
        return
    tem += abs(y - res)
    ans = min(ans, tem)

for x,y in arr[0]:
    bisect1(x,y)
for x,y in arr[1]:
    bisect2(x,y)
ans = -1 if ans == 9000000001 else ans
print(ans)