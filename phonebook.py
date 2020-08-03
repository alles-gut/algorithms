##programers.co.kr
##Hash - 전화번호 목록

def solution(phone_book):
    print(" ".join(phone_book))
    for elem in phone_book:
        if " ".join(phone_book).startswith(elem):
            print(1)
            print(elem)
            return False
    return True
