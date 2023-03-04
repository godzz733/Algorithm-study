arr = [0] * int(input())
t = int(input())
fake = real = num = real_num = 0
for i in range(1,t+1):
    a, b = map(int ,input().split())
    if b-a+1 > num:
        fake = i
        num = b-a+1
    for j in range(a-1,b):
        if not arr[j]:
            arr[j] = i
for i in range(1,t+1):
    if arr.count(i) > real_num:
        real = i
        real_num = arr.count(i)
print(fake)
print(real)