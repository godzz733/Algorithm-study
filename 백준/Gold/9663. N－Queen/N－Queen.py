n = int(input())
arr = [0] * n
cnt = 0
def promising(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x]-arr[i]) == abs(x-i):
            return False
    return True
def n_queen(x):
    global cnt
    if x==n:
        cnt += 1
        return
    for i in range(n):
        arr[x] = i
        if promising(x):
            n_queen(x+1)
n_queen(0)
print(cnt)