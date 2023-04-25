import sys

input = sys.stdin.readline


class segtree:
    def __init__(self, L):
        self.len = len(L)
        newL = []
        for i in L: newL.append([i, i, i, i])
        self.tree = [[0, 0, 0, 0] for i in range(self.len)] + newL
        for i in range(self.len - 1, 0, -1):
            L1 = self.tree[i]
            left = self.tree[2 * i]
            right = self.tree[2 * i + 1]
            L1[0] = max([left[0], left[2] + right[0]])
            L1[1] = max([right[1], right[2] + left[1]])
            L1[2] = left[2] + right[2]
            L1[3] = max([left[1] + right[0], left[3], right[3], L1[0], L1[1]])

    def res(self, now, start, end, left, right):
        if end < left or right < start:
            return [-1000000] * 4
        if left <= start and end <= right:
            return self.tree[now]
        mid = (start + end) // 2
        L1 = self.res(now * 2, start, mid, left, right)
        L2 = self.res(now * 2 + 1, mid + 1, end, left, right)
        L = []
        L.append(max(L1[0], L1[2] + L2[0]))
        L.append(max(L2[1], L2[2] + L1[1]))
        L.append(L1[2] + L2[2])
        L.append(max([L1[1] + L2[0], L1[3], L2[3], L[0], L[1]]))
        return L


n = int(input())
L = list(map(int, input().split()))
c = 1
while c < n: c *= 2
L += [0] * (c - n)
s = segtree(L)
for i in ' ' * int(input()):
    left, right = map(int, input().split())
    print(s.res(1, 1, c, left, right)[3])
