import sys; input = sys.stdin.readline
from itertools import product
import math
n = int(input())
if n == 1:
    print(2)
    print(3)
    print(5)
    print(7)
    exit()
arr = [1,3,7,9]
a = list(product(arr,repeat=n-1))
key = 1
for i in [2,3,5,7]:
    for j in a:
        tem = 10**(n-1) * i + int(''.join(map(str,j)))
        t = tem*10
        for k in range(n-1):
            t //= 10
            for q in range(2,math.ceil(math.sqrt(t)+1)):
                if t % q == 0:
                    key = 0
                    break
            if not key:
                break
        if key:
            print(tem)
        key = 1