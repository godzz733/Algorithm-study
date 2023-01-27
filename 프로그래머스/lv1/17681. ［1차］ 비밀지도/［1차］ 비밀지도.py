def solution(n, arr1, arr2):
    arr1_li = []
    arr2_li = []
    result = [[] for _ in range(n)]
    arr1_t = [[] for _ in range(n)]
    arr2_t = [[] for _ in range(n)]
    for i in range(n):
        a = format(arr1[i], 'b')
        arr1_li.append(a.zfill(n))
    for i in range(n):
        a = format(arr2[i], 'b')
        arr2_li.append(a.zfill(n))
    for i in range(n):
        for k in range(n):
            if arr1_li[i][k]=='0':
                arr1_t[i].append('0')
            else:
                arr1_t[i].append('#')
    for i in range(n):
        for k in range(n):
            if arr2_li[i][k]=='0':
                arr2_t[i].append('0')
            else:
                arr2_t[i].append('#')
    for i in range(n):
        for k in range(n):
            if arr1_t[i][k]=='0' and arr2_t[i][k]=='0':
                result[i].append(' ')
            elif arr1_t[i][k]=='#' or arr2_t[i][k]=='#':
                result[i].append('#')
    answer = list(map(''.join, result))

    return answer