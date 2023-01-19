a = str(input())
li = []
result = []
eval_li = []
for i in a:
    if i=='+' or i=='-':
        result.append(int(''.join(li)))
        result.append(i)
        li = []
    else:
        li.append(i)
result.append(int(float(''.join(li))))

for j in range(0,len(result)):
    if result[j] == '+':
        del eval_li[-1]
        result[j+1] = result[j-1]+result[j+1]
    else:
        eval_li.append(result[j])
print(eval(''.join(map(str,eval_li))))