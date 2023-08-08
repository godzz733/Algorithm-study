arr = []
map = {}
n = int(input())
for _ in range(n):
    tem = input()
    for j in range(len(tem)):
        if tem[j] not in map: map[tem[j]] = 0
        map[tem[j]] += 10**(len(tem)-j-1)
ans = 0
for key,value in map.items():
    arr.append([value,key])
arr.sort(key=lambda x : x[0],reverse=True)
idx = 9
for x,y in arr:
    ans += idx * x
    idx -= 1
print(ans)