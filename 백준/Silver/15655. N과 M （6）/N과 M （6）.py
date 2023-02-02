import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
arr = [*map(int,input().rstrip().split())]
arr.sort()
result = []
def back():
    if len(result) == m:
        print(*result)
        return
    for i in range(n):
        if arr[i] not in result:
            if result == []:
                result.append(arr[i])
                back()
                result.pop()
            elif arr[i]<max(result):
                pass
            else:
                result.append(arr[i])
                back()
                result.pop()

back()
