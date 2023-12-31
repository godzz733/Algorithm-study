def ispalin(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[-1-i]:
            return False
    return True
for T in range(1,int(input())+1):
    n,m = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    ispanlin = False
    same = 0
    for i in range(n):
        if arr[i][::-1] in arr[i+1:]:
            same += 2
        elif not ispanlin:
            ispanlin = ispalin(arr[i])
    if ispanlin:
        same += 1
    print(f'#{T}',same * m)