n, m = map(int, input().split())
li = [*map(int, input().split())]
li.sort()

result = set()
li_arr = []
def back():
    if len(li_arr) == m:
        if tuple(li_arr) not in result:
            result.add(tuple(li_arr))
            print(*li_arr)
            return
        else:
            return
    for i in li:
        if not li_arr:
            li_arr.append(i)
            back()
            li_arr.pop()

        elif i >= li_arr[-1]:
            li_arr.append(i)
            back()
            li_arr.pop()

back()
