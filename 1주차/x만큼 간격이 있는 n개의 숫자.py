def solution(x, n):
    answer = []
    
    cnt = x
    while len(answer) != n:
        answer.append(cnt)
        cnt += x
        
    return answer