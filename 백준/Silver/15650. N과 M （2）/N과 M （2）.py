n,m = map(int, input().split())
arr = []

def back():
    if len(arr) == m :
        print(' '.join(map(str,arr)))
        return
    for i in range(1,n+1):
        if i not in arr and (arr==[] or i > max(arr) ):
            arr.append(i)
            back()
            arr.pop()

back()
