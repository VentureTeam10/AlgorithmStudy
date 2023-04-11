def solution(x, n):
    answer = []
    none = 0
    for i in range(n):
        none += x
        answer.append(none)
    return answer
