def solution(expression):
    tem = ""
    arr = []
    ja = ["*","-","+"]
    for i in expression:
        if i in ja:
            arr.append(int(tem))
            arr.append(i)
            tem = ""
        else:
            tem += i
    arr.append(int(tem))
    answer = 0
    answer = max(cal(arr, ["*","+","-"]),cal(arr, ["*","-","+"]),cal(arr, ["-","+","*"]),cal(arr, ["-","*","+"]),cal(arr, ["+","*","-"]),cal(arr, ["+","-","*"]))
    return answer

def cal(arr,priority):
    tem = arr
    temp = []
    for j in priority:
        idx = 0
        while(idx < len(tem)):
            if tem[idx] != j:
                temp.append(tem[idx])
                idx += 1
            else:
                if j == "*":
                    temp.append(temp.pop() * tem[idx+1])
                    idx += 2
                elif j == "+":
                    temp.append(temp.pop() + tem[idx+1])
                    idx += 2
                else:
                    temp.append(temp.pop() - tem[idx+1])
                    idx += 2
        tem = temp
        temp = []
    return abs(tem[0])
                    
                
            
        