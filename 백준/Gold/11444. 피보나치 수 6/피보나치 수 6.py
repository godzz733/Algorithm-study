from math import log2


def matmul_2x2(a, b):
    # 2x2 행렬 곱셈
    return_mat = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                return_mat[i][j] += a[i][k] * b[k][j]
                return_mat[i][j] %= 1000000007
    return return_mat


def to_reverse_bin(n: int):
    return_array = [0 for _ in range(int(log2(n)) + 1)]
    while n > 0:
        temp_lg2n = int(log2(n))
        return_array[temp_lg2n] += 1
        n -= 2 ** temp_lg2n

    return return_array


def fib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    binarr = to_reverse_bin(n - 1)
    # 또는 python의 내장 라이브러리 함수 bin()을 이용하여
    # binarr = list(map(int, reversed(bin(n-1)[2:])))

    m_powers = []
    m_powers.append(
        [[1, 1],
         [1, 0]]
    )

    for i in range(1, len(binarr)):
        m_powers.append(matmul_2x2(m_powers[-1], m_powers[-1]))

    final_mat = [
        [1, 0],
        [0, 1]
    ]
    for i in range(len(binarr)):
        if binarr[i]:
            final_mat = matmul_2x2(m_powers[i], final_mat)

    return final_mat[0][0]

n = int(input())
print(fib(n))