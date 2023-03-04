n, k = map(int, input().split())
arr = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
room = 0
for _ in range(n):
    a, b = map(int, input().split())
    arr[b-1][a] += 1
for x, y in arr:
    if not x and not y:
        continue
    room += x//k + x%k
    room += y//k + y%k
print(room)