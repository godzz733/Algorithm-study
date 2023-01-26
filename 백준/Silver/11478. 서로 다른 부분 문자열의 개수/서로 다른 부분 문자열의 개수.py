import sys

st = str(input())
dic = {}


for k in range(1,len(st)):
    for j in range(len(st)-k):
        dic[st[j:j+k]] = 1
    dic[st[len(st)-k:]] = 1

print(sum(list(dic.values()))+1)