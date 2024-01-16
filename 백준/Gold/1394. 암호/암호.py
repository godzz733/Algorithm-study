a = list(input())
dic = {a[i]:i+1 for i in range(len(a))}
b = list(input())
arr = [0,len(a)]
def mod(x):
    return x%900528
for i in range(len(b)-1):
    arr.append(mod(arr[-1]*len(a)))
ans = 0
for i in range(1,len(b)):
    ans += arr[i]
    ans = mod(ans)
for j in range(len(b)-1):
    ans += arr[len(b)-j-1]*(dic[b[j]]-1)
    ans = mod(ans)
print((ans+dic[b[-1]])%900528)