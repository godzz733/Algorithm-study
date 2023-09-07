import math
def solution(r1, r2):
    answer = 0
    a = b = 0
    for i in range(1,r2):
        tem = r1**2 - i**2
        if tem <0: tem = 0
        else:
            if tem != 0 and (r1**2-i**2)**(1/2) == math.floor((r1**2-i**2)**(1/2)): a += 1
            tem = math.floor(tem**(1/2))
        a += math.floor((r2**2 - i**2)**(1/2)) - tem
    return a*4 + b + (r2-r1+1) * 4
