import sys; input = sys.stdin.readline
from itertools import combinations

n = int(input())
arr = [1,1]
for i in range(2,20):
    arr.append(arr[-1] * i)

for i in range(1,21):
    for j in combinations(arr,i):
        if sum(j) == n:
            print("YES")
            exit()
else:
    print("NO")