a = [0,1]
n = int(input())
for i in range(n-1):a.append(a[-1]+a[-2])
print(a[n])