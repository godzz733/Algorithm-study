while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]

    count = 0


    def dfs(x, y):
        if x < 0 or x >= h or y < 0 or y >= w:
            return False
        if arr[x][y] == 1:
            arr[x][y] = 0
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x - 1, y - 1)
            dfs(x - 1, y + 1)
            dfs(x + 1, y - 1)
            dfs(x + 1, y + 1)
            return True
        else:
            return False


    for i in range(w):
        for j in range(h):
            if dfs(j, i):
                count += 1
    print(count)
