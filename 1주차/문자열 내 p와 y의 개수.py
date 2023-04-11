def solution(s):
    p_num = 0
    y_num = 0
    s = s.lower()
    answer = True
    for i in range(len(s)):
        if s[i] == 'p':
            p_num += 1
        elif s[i] == 'y':
            y_num += 1
    answer = p_num == y_num
    return answer
