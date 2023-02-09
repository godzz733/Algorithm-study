n, m = map(int, input().split())
li = [*map(int, input().split())]
li.sort()
arr = []
for j, i in enumerate(li):
    arr.append((i, j))

result = set()
li_arr = []
idx_arr = []
def back():
    if len(li_arr) == m:
        if tuple(li_arr) not in result:
            result.add(tuple(li_arr))
            print(*li_arr)
            return
        else:
            return
    for i, j in arr:
        if not li_arr:
            idx_arr.append(j)
            li_arr.append(i)
            back()
            li_arr.pop()
            idx_arr.pop()
        elif j not in idx_arr and i>=li_arr[-1]:
            idx_arr.append(j)
            li_arr.append(i)
            back()
            li_arr.pop()
            idx_arr.pop()

back()
