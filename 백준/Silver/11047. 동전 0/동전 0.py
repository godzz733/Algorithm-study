n,k = map(int,input().split()) # 배수 그리디 문제
coin = []
for i in range(n):
    a = int(input())
    coin.append(a)

num = 0
for j in coin[::-1]:
    if k//j !=0:
        num += k//j
        k = k - (k//j)*j

print(num)