
t = int(input())
arr =[]
so = []
result = []
for _ in range(t):
    a= str(input())
    if a not in arr: #중복 제거
        arr.append(a)

arr.sort(key=lambda x:len(x)) #문자열 길이로 일단 정렬
for i in range(0,len(arr)):  #이제 길이별로 나눠서 사전 순서로 정렬
    if i == (len(arr)-1):
        if so!=[] and len(so[-1]) == len(arr[i]):
            so.append(arr[i])
            so.sort()
            [result.append(x) for x in so]
        elif so ==[]:
            so.append(arr[i])
            result.append(arr[i])
        elif so!=[] and len(so[-1]) != len(arr[i]):
            so.sort()
            [result.append(x) for x in so]
            so.append(arr[i])
            result.append(arr[i])
    elif so ==[]:
        so.append(arr[i]) 
    elif len(arr[i]) == len(so[0]):
        so.append(arr[i])
    else:
        so.sort()
        [result.append(x) for x in so]
        so = []
        so.append(arr[i])

[print(j) for j in result]