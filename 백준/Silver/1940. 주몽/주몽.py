n = int(input())
m = int(input())
arr = [0] * (100001)
tem = list(map(int, input().split()))
for i in tem:arr[i] += 1
if m > 200000: print(0)
else:
    ans = 0
    for i in range(100001):
        if m - i > 100000: continue
        ans += arr[i] * arr[m - i]
        if i == m//2  and m%2 == 0: ans -= arr[i]
    print(ans//2)