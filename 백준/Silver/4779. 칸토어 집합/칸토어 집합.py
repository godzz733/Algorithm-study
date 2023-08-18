def can(lst):
    if len(lst) == 1:
        return ['-']
    size = len(lst)//3
    return can(lst[:size]) + [' ' for _ in range(size)] + can(lst[2*size:])
while 1:
    try:
        n = int(input())
        arr = ['-' for _ in range(3**n)]
        ans = can(arr)
        for i in range(len(ans)-1):
            print(ans[i],end='')
        print(ans[len(ans)-1])
    except:
        break
