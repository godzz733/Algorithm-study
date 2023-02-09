m, n = map(int, input().split())
li = [*map(str, input().split())]
li.sort()
alp = ['a', 'e', 'i', 'o', 'u']

li_arr = []


def back():
    if len(li_arr) == m:
        cnt = 0
        for i in alp:
            cnt += li_arr.count(i)
        if cnt > 0:
            if m-cnt>=2:
                print(''.join(li_arr))
                return
        else:
            return

    for i in li:
        if not li_arr:
            li_arr.append(i)
            back()
            li_arr.pop()

        elif i >= li_arr[-1] and i not in li_arr:
            li_arr.append(i)
            back()
            li_arr.pop()


back()