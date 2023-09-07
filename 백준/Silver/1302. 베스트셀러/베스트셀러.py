dic = {}
for i in range(int(input())):
    tem = input()
    if tem not in dic:dic[tem] = 1
    else: dic[tem] += 1
arr = [(a,b) for a,b in dic.items()]
arr.sort(key=lambda x:(-x[1],x[0]))
print(arr[0][0])