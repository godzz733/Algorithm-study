arr = []
for _ in range(5):
    lst = list(input())
    while len(lst) != 15:
        lst.append(' ')
    arr.append(lst)
ans = ""
for i in range(15):
    for j in range(5):
        if arr[j][i] != ' ':
            ans += arr[j][i]
print(ans)