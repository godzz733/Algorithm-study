import copy
n = int(input())
ori = [list(map(int, input().split())) for _ in range(n)]
lst = [(0,5),(1,3),(2,4),(3,1),(4,2),(5,0)]
result = []
for i in lst:
    cnt = 0
    num = [1,2,3,4,5,6]
    a = ori[0][i[0]]
    b = ori[0][i[1]]
    num.remove(a)
    num.remove(b)
    cnt += max(num)
    for k in range(1,n):
        num = [1, 2, 3, 4, 5, 6]
        a = b
        b = ori[k][lst[ori[k].index(a)][1]]
        num.remove(a)
        num.remove(b)
        cnt += max(num)
    result.append(cnt)
print(max(result))