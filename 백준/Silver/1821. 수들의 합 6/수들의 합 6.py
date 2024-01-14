import sys; input = sys.stdin.readline
from itertools import permutations
n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]
def check(arr):
    while len(arr) != 1:
        tem = []
        for i in range(len(arr)-1):
            tem.append(arr[i]+arr[i+1])
        if sum(tem) > m:
            return False
        arr = tem
    if arr[0] == m:
        return True
    return False
for i in permutations(arr,n):
    if check(list(i)):
        print(*i)
        break