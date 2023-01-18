n,k = map(int,input().split())

li = [i for i in range(1,n+1)]
result = []

while len(li)>2: #li 요소가 2개 될때까지 k번째를 제거할거임
    if len(li)>k: #li가 k보다 크면 그냥 k번째를 result에 넣고 슬라이싱
        result.append(li[k-1])
        li = li[k:] + li[0:k-1]
    elif len(li) == k:
        result.append(li[k-1])
        li = li[0:k-1]
    elif len(li)<k:
        if k%(len(li))==0:
            result.append(li[k%len(li)-1])
            li = li[0:len(li)-1]
        else:
            result.append(li[k%len(li)-1])
            li = li[k%len(li):] + li[0:k%len(li)-1]

if k%2==0: #k가 짝수면 li의 두번째가 먼저 들어감
    result.append(li[1])
    result.append(li[0])
elif k%2==1: #k가 홀수면 li의 첫번째가 먼저 들어감
    if n==1:
        result.append(li[0])
    else:
        result.append(li[0])
        result.append(li[1])



print('<',end='')
[print(x, end=', ') for x in result[0:n-1]]
print(f'{result[n-1]}>')