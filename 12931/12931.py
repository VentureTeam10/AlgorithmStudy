#자릿수 더하기
def solution(n):
    answer = 0
    str_n = str(n)
    for i in str_n:
        answer += int(i)

    return answer
