t = int(input())
num2 = 0
num5 = 0
for i in range(2,t+1):
    for k in range(1,9):
        if i%(2)==0:
            num2 +=1
            i = int(i/2)

    for j in range(1,4):
        if i%(5)==0:
            num5 +=1
            i = int(i/5)

if num2 == num5:
    print(num2)
elif num2>num5:
    print(num5)
else:
    print(num2)
    