from fractions import Fraction
n = int(input())
a = [*map(str, input().split())]
b = [*map(str,input().split())]
b += b
b.pop()
dp = [0] * len(a)
j = 0
cnt = 0
for i in range(1,len(a)):
    while (j>0 and a[i] != a[j]):
        j = dp[j-1]
    if a[i] == a[j]:
        dp[i] = j+1
        j += 1
j = 0
for i in range(0,len(b)):
    while j>0 and b[i] != a[j]:
        j = dp[j-1]
    if b[i] == a[j]:
        if j==len(a)-1:
            cnt += 1
            j = dp[j]
        else:
            j += 1
a = Fraction(cnt,n)
if a == 1:
    print("1/1")
else:
    print(a)