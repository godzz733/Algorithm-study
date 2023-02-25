n = int(input())
arr = [0] * (1001)
result = 0
for _ in range(n):
    a, b = map(int,input().split())
    arr[a] = b
st = en = 0
for i in range(1001):
    if arr[i]:
        st = i
        break
for i in range(1000,-1,-1):
    if arr[i]:
        en = i
        break
midx = arr.index(max(arr))
left = right = 0
while st<=midx:
    if arr[st] > left:
        left = arr[st]
    result += left
    st += 1
while midx<en:
    if arr[en] > right:
        right = arr[en]
    result += right
    en -= 1
print(result)