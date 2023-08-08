import sys
input = sys.stdin.readline
arr, map = [0 for _ in range(26)] ,{}
for _ in range(int(input())):
    tem = input().rstrip()
    for j in range(len(tem)):
        arr[ord(tem[j])-ord('A')] += 10 ** (len(tem) - j -1)
ans = 0
arr.sort(reverse=True)
idx = 9
for i in range(10):
    ans += idx * arr[i]
    idx -= 1
print(ans)