def solution(nums):
    answer = 0
    
    length = len(nums) // 2
    myList = list(set(nums))
    
    if length >= len(myList):
        answer = len(myList)
    
    else:
        answer = length
    return answer