arr = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
def solution(numbers, hand):
    leftnow = (3,0)
    rightnow = (3,2)
    answer = ''
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            leftnow = arr[i]
            answer += "L"
        elif i == 3 or i == 6 or i == 9:
            rightnow = arr[i]
            answer += "R"
        else:
            left = find_radian(leftnow,i)
            right = find_radian(rightnow,i)
            if left < right:
                answer += "L"
                leftnow = arr[i]
            elif left > right:
                answer += "R"
                rightnow = arr[i]
            else:
                if hand == "right":
                    answer += "R"
                    rightnow = arr[i]
                else:
                    answer += "L"
                    leftnow = arr[i]
    return answer

def find_radian(hand, num):
    global arr
    return abs(arr[num][0]-hand[0])+abs(arr[num][1]-hand[1])