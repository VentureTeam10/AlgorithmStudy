def solution(num):
    answer = ''
    
    # 짝수
    if num % 2 == 0:
        answer = 'Even'
    
    # 홀수 
    else:
        answer = 'Odd'
    return answer