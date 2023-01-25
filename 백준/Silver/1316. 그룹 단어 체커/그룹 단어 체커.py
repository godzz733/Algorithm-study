t = int(input())
count = 0
for i in range(t):
    dic = {}
    a = str(input())
    li = list(a)
    for i in range(len(li)):
        if li[i] not in dic:
            dic[li[i]]=1
        else:
            if li[i]!=li[i-1]:
                dic[li[i]]+=1
    key = 0
    for i in list(dic.values()):
        if i >1:
            key+=1
    if key==0:
        count +=1
    else:
        pass
print(count)
    