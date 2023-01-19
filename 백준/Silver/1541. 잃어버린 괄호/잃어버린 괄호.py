a = str(input())
li = []
result = [] #상수와 연산자 구분해서 담음
eval_li = [] # +를 미리 처리(알맞게 괄호를 친것과 같은 효과)하고 남은 것들을 식 형태로 보관 
for i in a: #먼저 입력 값을 상수와 연산자로 구분함
    if i=='+' or i=='-':
        result.append(int(''.join(li)))
        result.append(i)
        li = []
    else:
        li.append(i)
result.append(int(float(''.join(li))))

for j in range(0,len(result)):
    if result[j] == '+':  #만약 +가 있다면 앞뒤로 더한뒤 기존 리스트에 넘겨줌
        del eval_li[-1]
        result[j+1] = result[j-1]+result[j+1]
    else:
        eval_li.append(result[j])
print(eval(''.join(map(str,eval_li)))) #결과적으로 +는 다 하고 -만 남아서 의도에 맞게 괄호를 친 결과가 되었고 마지막으로 남은 -들은 eval함수로 계산함
