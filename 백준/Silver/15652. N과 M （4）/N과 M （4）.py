n,m = map(int, input().split())
arr = []

def back():
    if len(arr) == m :
        print(' '.join(map(str,arr)))
        return
    for i in range(1,n+1):
        if arr==[] or i>=arr[-1]: # 비내림차순이라 i가 이미 있는거보다 크거나 같다라는 조건 추가
            arr.append(i)
            back()
            arr.pop()

back()
