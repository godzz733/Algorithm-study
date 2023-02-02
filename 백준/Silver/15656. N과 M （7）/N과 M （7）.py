n, m = map(int ,input().split())
arr = [*map(int, input().split())]
arr.sort()
result = []
def back():
    if len(result) == m:
        print(*result)
        return
    for i in range(n):
        result.append(arr[i])
        back()
        result.pop()
back()
