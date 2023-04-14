def solution(id_list, report, k):
    dic = {}
    num = {}
    for i in range(len(id_list)):
        dic[id_list[i]] = set()
        num[id_list[i]] = i
    for i in range(len(report)):
        a, b = report[i].split()
        dic[b].add(a)
    answer = [0] * len(id_list)
    for a in id_list:
        if len(dic[a])>=k:
            for i in dic[a]:
                answer[num[i]] += 1
    
    
    return answer