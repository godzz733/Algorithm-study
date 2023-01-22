queue = []
t= int(input())
for i in range(t):
    a = int(input())
    if a !=0:
        queue.append(a)
    else:
        queue.pop()

print(sum(queue))

