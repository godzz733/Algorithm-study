import sys

inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())
row = [0, n]
col = [0, m]
t = int(inp())
for i in range(t):
    a, b = map(int, inp().rstrip().split())
    if a == 0:
        col.append(b)
    else:
        row.append(b)
result_row = []
result_col = []
row.sort()
col.sort()

for i in range(1, len(row)):
    result_row.append(row[i]-row[i-1])
for i in range(1, len(col)):
    result_col.append(col[i]-col[i-1])

print(max(result_row)*max(result_col))
