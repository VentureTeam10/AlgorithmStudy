#x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    none = 0
    for i in range(n):
        none += x
        answer.append(none)
    return answer
