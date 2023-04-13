def solution(participant, completion):
    answer = ''
    dic_completion = {}
    dic_participant ={}

    for c in completion:                                                        //딕셔너리에 완주자 이름 넣기
        if dic_completion.get(c) != None:       
            dic_completion[c] += 1
        else:
            dic_completion[c] = 1

    for p in participant:                                                       //딕셔너리에 참가자 이름 넣기
        if p in dic_participant:
            dic_participant[p] += 1
        else:
            dic_participant[p] = 1

        if p not in dic_completion:                                             //참가자의 이름이 완주자에 포함이 안됐을 때
            answer = p
        elif p in dic_completion and dic_completion[p] < dic_participant[p]:    //동명이인의 참가자인 경우 완주자의 수보다 참가자의 수가 더 큰 경우
            answer = p
        
    return answer
