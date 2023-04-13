#나머지가 1이되는 수 찾기

def solution(n):
    answer = 2
    while n % answer != 1:
        if answer > n/2:
            answer = n - 1
        else:
            answer += 1
    return answer