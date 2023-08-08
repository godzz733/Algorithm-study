n,m = map(int,input().split())
arr = list(input())
a,b,c,d = map(int,input().split())
dic = {'A':a,'C':b,'G':c,'T':d}
tem = {'A':a,'C':b,'G':c,'T':d}
st =0
fi = m
cnt = 0
ans = {'A':0,'C':0,'G':0,'T':0}
for i in range(m):
    ans[arr[i]] += 1
def isDNA(arr):
    for key,val in arr.items():
        if val < dic[key]: return 0
    return 1
cnt += isDNA(ans)
while fi<n:
    ans[arr[st]] -= 1
    ans[arr[fi]] += 1
    cnt += isDNA(ans)
    st += 1
    fi += 1
print(cnt)