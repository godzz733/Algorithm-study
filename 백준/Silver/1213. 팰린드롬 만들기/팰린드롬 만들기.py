import sys; input = sys.stdin.readline

t = list(input().rstrip())
n = len(t)
dic = {}
for i in t:
    dic[i] = dic.get(i, 0) + 1
num = 0
for i in dic.values():
    if i & 1: num += 1
if num > 1:
    print("I'm Sorry Hansoo")
    exit()
if n & 1:
    if not num:
        print("I'm Sorry Hansoo")
        exit()
    ans = [""] * n
    for i in dic:
        if dic[i] & 1:
            ans[n//2] = i
            dic[i] -= 1
            break
    idx = 0
    for i in sorted(dic):
        while dic[i]:
            ans[idx] = ans[n-idx-1] = i
            dic[i] -= 2
            idx += 1
else:
    if num:
        print("I'm Sorry Hansoo")
        exit()
    ans = [""] * n
    idx = 0
    for i in sorted(dic):
        while dic[i]:
            ans[idx] = ans[n-idx-1] = i
            dic[i] -= 2
            idx += 1
print("".join(ans))