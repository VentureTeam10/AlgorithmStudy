def solution(clothes):
    answer = 1
    hanger_dict = {}
    
    for clo in clothes :
        if clo[1] not in hanger_dict.keys() :
            hanger_dict[ clo[1] ] = 1
        else :
            hanger_dict[ clo[1] ] += 1
    
    for key, value in hanger_dict.items() :
        answer *= ( value + 1 ) 
        
    answer -= 1
        
    return answer