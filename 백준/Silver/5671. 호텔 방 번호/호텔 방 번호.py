import sys; input = sys.stdin.readline
from collections import Counter
arr = [0]
for i in range(1,5001):
    if Counter(str(i)).most_common()[0][1] == 1:
        arr.append(arr[-1]+1)
    else:
        arr.append(arr[-1])
while 1:
    try:
        n,m = map(int, input().split())
        print(arr[m]-arr[n-1])
    except:
        break