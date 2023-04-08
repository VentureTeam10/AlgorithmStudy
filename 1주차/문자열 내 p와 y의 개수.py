def solution(s):
    answer = True
    
    countP = 0
    countY = 0
    
    for ch in s:
        if (ch == 'P') or (ch == 'p'):
            countP += 1
            
        elif (ch == 'Y') or (ch == 'y'):
            countY += 1
    
    if countP != countY:
        answer = False

    return answer