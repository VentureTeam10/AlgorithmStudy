#프로세스
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(enumerate(priorities))  

    while queue:
        cur = queue.popleft()  
        higher_priority = False
        
        for q in queue:
            if cur[1] < q[1]:  
                higher_priority = True
                break
        
        if higher_priority:
            queue.append(cur)  
        else:
            answer += 1  
            if cur[0] == location:  
                return answer
