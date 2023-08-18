n,m = map(int,input().split())
dic = {}
for _ in range(n):
    tem = input()
    if len(tem) < m:continue
    if (tem,len(tem)) not in dic:dic[(tem,len(tem))]=1
    else:dic[(tem,len(tem))]+=1
ans = []
for x,y in dic.items():
    ans.append((y,x[1],x[0]))
ans.sort(key=lambda x: (-x[0],-x[1],x[2]))
for x,y,z in ans:print(z)