def solution(s):
    answer = 1001
    # 1개가 들어올 경우 1 return
    if len(s) == 1:
        return 1
    
    # s의 길이의 절반까지 나눈 압축의 최소값을 구한다.
    for i in range(1,len(s) // 2 + 1):
        stack = []
        cnt = 1
        now_result = ""
        cur_word = ""
        # i로 현재에서 나눈 단어를 비교해본다
        for word in range(len(s)):
            # 현재 단어를 더해준다
            cur_word += s[word]
                
            
            # 만약 cur_word가 i와 같으면 아래단계진행
            if len(cur_word) == i:
            # 아직 아무 단어도 저장 안되어있다면
                if len(stack) == 0:
                    stack.append(cur_word)
                    cur_word = ""
                # 바로 전의 단어가 저장되어 있다면
                else:
                    # 바로전의 단어와 같다면 cnt를 올려준다
                    if stack[0] == cur_word:
                        cnt += 1
                        cur_word = ""
                    # 바로 전의 단어와 다르면 전의단어를 now_result에 저장
                    # 그 후 현재의 단어를 stack에 저장
                    else:
                        prev_word = stack.pop()
                        if cnt == 1:
                            now_result += prev_word
                        else:   
                            now_result += str(cnt) + prev_word
                            cnt = 1
                        stack.append(cur_word)
                        cur_word = ""
        if cnt != 1:
            now_result += str(cnt) + stack.pop()
        else:
            now_result += stack.pop()
        now_result += cur_word
        answer = min(len(now_result), answer)
    
    return answer