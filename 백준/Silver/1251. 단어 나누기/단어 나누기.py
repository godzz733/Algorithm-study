arr= input()
ans = 'z' * 100
for i in range(1,len(arr)-1):
    for j in range(i+1,len(arr)):
        ans = min(ans,''.join(reversed(arr[:i])) + ''.join(reversed(arr[i:j])) + ''.join(reversed(arr[j:])))
print(ans)