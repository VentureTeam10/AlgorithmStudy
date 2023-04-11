def solution(participant, completion):
    answer = ''
    dic_completion = {}
    dic_participant ={}

    for c in completion:
        if dic_completion.get(c) != None:
            dic_completion[c] += 1
        else:
            dic_completion[c] = 1

    for p in participant:
        if p in dic_participant:
            dic_participant[p] += 1
        else:
            dic_participant[p] = 1

        if p not in dic_completion:
            answer = p
        elif p in dic_completion and dic_completion[p] < dic_participant[p]:
            answer = p
        
    return answer
