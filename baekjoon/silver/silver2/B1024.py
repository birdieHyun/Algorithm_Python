def solution(phone_book):

    hash_map = {}

    for phone in phone_book:
        hash_map[phone] = 1

    for phone_number in phone_book:
        prefix = ""
        for number in phone_number:
            prefix += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if prefix in hash_map and prefix != phone_number:
                return False
    return True


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))