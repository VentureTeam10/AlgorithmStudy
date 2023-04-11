#폰켓몬

def solution(nums):
    cnt = len(nums) // 2

    monster = list(set(nums))
    if len(monster) < cnt:
        return len(monster)

    return cnt
