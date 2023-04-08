def solution(participant, completion):
    answer = ''
    dic_completion = {}
    
    for c in completion:
        if dic_completion.get(c) != None:
            dic_completion[c] = dic_completion[c] + 1
            
        else:
            dic_completion[c] = 1
        
    for p in participant:
        if (dic_completion.get(p) != None) and (dic_completion.get(p) != 0):
            dic_completion[p] = dic_completion[p] - 1
            
        else:
            answer = p
            break
        
    return answer