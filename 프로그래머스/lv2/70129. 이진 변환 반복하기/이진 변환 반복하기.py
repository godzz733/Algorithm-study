def solution(s):
    arr = s
    a = b = 0
    cnt = 1
    while len(arr) != 1:
        a += len(list(arr)) - len(list(''.join(arr.split("0"))))
        arr = bin(len(''.join(arr.split("0"))))[2:]
        cnt += 1
                     
    answer = [cnt-1,a]
    return answer