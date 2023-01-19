n,m = map(int, input().split())
arr = []

def back():
    if len(arr) == m :
        print(' '.join(map(str,arr)))
        return
    for i in range(1,n+1): #그냥 not in 조건을 뺏음
        arr.append(i)
        back()
        arr.pop()

back()