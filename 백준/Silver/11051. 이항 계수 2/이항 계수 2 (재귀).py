import sys
sys.setrecursionlimit(1001)
def factorial(N):
    if N == 1 or N == 0:
        return 1
    else:
        return factorial(N-1) * N

N, K = map(int,input().split())
result = factorial(N) // (factorial(N-K) *factorial(K))
print(result % 10007)
