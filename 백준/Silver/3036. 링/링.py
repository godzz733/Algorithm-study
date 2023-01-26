from fractions import Fraction
t = int(input())

arr = [*map(int,input().split())]
for i in range(1,t):
    if arr[0]%arr[i] ==0:
        print(f'{int(arr[0]/arr[i])}/1')
    else:
     print(Fraction(arr[0],arr[i]))

