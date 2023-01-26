from fractions import Fraction
n,k = map(int,input().split())

arr = [[0 for _ in range(n+2)] for _ in range(n+2)]

arr[0][0] = 1

narr = [1]
npac =1
for i in range(1,1003):
    npac *=i
    narr.append(npac)

for i in range(1,n+2):
    for j in range(0,i//2+1):
        arr[i][j] = int(narr[i]//(narr[j]*narr[i-j]))
        arr[i][i-j] = arr[i][j]

print(arr[n][k]%10007)




