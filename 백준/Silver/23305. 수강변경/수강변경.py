n,arr,arr2 = open(0)
a = [0] * (int(1e6)+1)
for i in map(int, arr.split()):
    a[i] += 1
for i in map(int, arr2.split()):
    a[i] -= 1
ans = 0
for i in a:
    ans += abs(i)
print(ans>>1)