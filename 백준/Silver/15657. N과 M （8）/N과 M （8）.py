n, m = map(int ,input().split())
arr = [*map(int, input().split())]
arr.sort()
result = []
def back():
    if len(result) == m:
        print(*result)
        return
    for i in range(n):
        if result == []:
            result.append(arr[i])
            back()
            result.pop()
        else:
            if arr[i]>=max(result):
                result.append(arr[i])
                back()
                result.pop()
back()
