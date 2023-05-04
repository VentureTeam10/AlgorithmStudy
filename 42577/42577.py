#전화번호 목록
def solution(phone_book):
    phone_set = set(phone_book)
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in phone_set:
                return False
    return True
