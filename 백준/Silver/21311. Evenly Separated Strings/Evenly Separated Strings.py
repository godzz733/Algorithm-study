import sys; input = sys.stdin.readline
st = input().rstrip()
dic = {}
for i in range(len(st)):
    if st[i] in dic:
        if dic[st[i]][i & 1] == 1:
            print("NO")
            exit()
        dic[st[i]][i & 1] = 1
    else:
        dic[st[i]] = [0,0]
        dic[st[i]][i & 1] = 1
print("YES")