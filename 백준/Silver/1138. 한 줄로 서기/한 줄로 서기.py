import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
st = []
ans = []
for i in range(n-1,-1,-1):
    if arr[i] == len(ans):
        st.append(i+1)
    elif arr[i] < len(ans):
        ans.insert(arr[i], i+1)
    else:
        while st and arr[i] > len(ans):
            ans.append(st.pop())
        ans.append(i+1)
while st:
    ans.append(st.pop())
print(*ans)