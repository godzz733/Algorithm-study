arr = list(input())
size = len(arr)
ans = set()
visited = [False] * size
def back(cnt,lst):
    global ans
    if cnt == size:
        ans.add(''.join(lst))
        return
    for i in range(size):
        if visited[i]: continue
        if cnt == 0:
            lst.append(arr[i])
            visited[i] = True
            back(cnt+1,lst)
            visited[i] = False
            lst.pop()
        else:
            if lst[cnt-1] != arr[i]:
                lst.append(arr[i])
                visited[i] = True
                back(cnt+1,lst)
                visited[i] = False
                lst.pop()
back(0,[])
print(len(ans))