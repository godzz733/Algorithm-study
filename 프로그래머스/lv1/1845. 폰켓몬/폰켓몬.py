def solution(nums):
    mon = set(nums)
    answer = 0
    if len(mon) >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(mon)
    return answer