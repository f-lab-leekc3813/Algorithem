def solution(phone_book):
    # 해시테이블 생성
    hash_table = {}
    # phone_book을 해시화
    for char in phone_book:
        hash_table[char] = 1
    # 모든 원소를 체크
    for cur_char in phone_book:
        # 접두어 선언
        jubdoo = ""
        # 해당 문자의 접두어 체크
        for cur_num in cur_char:
            jubdoo += cur_num
            if jubdoo in hash_table and jubdoo != cur_char:
                return False
        
    return True