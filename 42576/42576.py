# 완주하지 못한 선수

def solution(participant, competion) :
    answer = ''
    temp = 0
    dic = {}
    for part in participant :
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in competion :
        temp -= hash(com)
    answer = dic[temp]

    return answer
