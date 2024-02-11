def solution(sequence):
    answer = 0
    a = [(-1) ** i for i in range(len(sequence))] + [0]
    for i in range(len(sequence)):
        a[i] *= sequence[i]

    for i in range(1,len(sequence)):
        a[i] += a[i-1]

    return abs(max(a)-min(a))