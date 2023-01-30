import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
check = [0] * (257)
time = []
result = []

for _ in range(n):
    arr = [*map(int,input().split())]
    for i in arr:
        check[i] +=1
for i in range(257):
    num = 0
    block = b
    for k in range(256,-1,-1):
        if k>i:
            block += (k-i)*check[k]
            num += (k-i)*2*check[k]
        elif k<i:
            block -= (i-k)*check[k]
            if block<0:
                break
            num += (i-k)*check[k]
    if block<0:
        pass
    else:
        time.append((num,i))
for i in sorted(time):
    if i[0]==sorted(time)[0][0]:
        result.append(i)
print(*result[-1])