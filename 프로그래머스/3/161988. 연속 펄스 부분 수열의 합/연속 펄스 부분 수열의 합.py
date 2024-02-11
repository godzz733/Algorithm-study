def solution(sequence):
    answer = 0
    a = [(-1) ** i for i in range(len(sequence))]
    b = [(-1) ** i for i in range(1,len(sequence)+1)]
    for i in range(len(sequence)):
        a[i] *= sequence[i]
        b[i] *= sequence[i]
    for i in range(1,len(sequence)):
        a[i] += a[i-1]
        b[i] += b[i-1]
    tem = 0
    for i in range(len(sequence)):
        answer = max(a[i] - tem, answer)
        tem = min(a[i],tem)
    tem = 0
    for i in range(len(sequence)):
        answer = max(b[i] - tem, answer)
        tem = min(b[i],tem)
    return answer