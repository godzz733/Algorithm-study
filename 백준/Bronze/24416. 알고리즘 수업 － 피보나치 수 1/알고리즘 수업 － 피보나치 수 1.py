count = 0
count2 = 0
a = int(input())
result = [0 for _ in range(a+1)]
result[1] = 1
result[2] = 1
def fibo(n):
    global count
    if n==1 or n==2:
        count +=1
        return 1
    count +=1
    return fibo(n-2)+fibo(n-1)
for i in range(3,a+1):
    result[i] = result[i-1] + result[i-2]
    count2+=1


print(fibo(a),count2)