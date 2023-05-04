#의상
def solution(clothes):
    dic = {}
    for cloth, category in clothes:
        if category in dic:
            dic[category].append(cloth)
        else:
            dic[category] = [cloth]
    
    answer = 1
    for key in dic:
        answer *= len(dic[key]) + 1 
    return answer - 1 
