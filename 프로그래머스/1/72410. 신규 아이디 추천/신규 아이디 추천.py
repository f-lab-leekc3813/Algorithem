def solution(new_id):
    # 주어진 문자열의 모든 대문자를 대응되는 소문자로 치환한다
    step1 = new_id.lower()
    
    # 주어진 문자열에서 알파벤 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문제를 제거한다
    step2 = ""
    
    for c in step1:
        # isalpha는 알파벳인지 확인
        # isdigit는 숫자인지 확인
        if c.isalpha() or c.isdigit() or c in "-_.":
            step2 += c
            
    # 주어진 문자열에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in step2:
        step2 = step2.replace('..', '.')
        
    step3 = step2[:]
    # 주어진 문자열에서 처음과 끝에 위치한 마침표(.)를 제거한다.
    # strip은 처음과 끝을 확인하여 해당 문자열이 존재하면 제거한다
    step4 = step3.strip('.')
    
    # 주어진 문자열이 빈 문자열이라면, "a"를 대입한다.
    if step4 == "":
        step5 = "a"
    else:
        step5 = step4[:]
    
    # 주어진 문자열의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거한다.
    # 제거 후 마침표(.)가 문자열의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거한다.
    step6 = step5[:15].rstrip('.')
    
    # 주어진 문자열의 길이가 2자 이하라면, 마지막 문자를 문자열의 길이가 3이 될 때까지 반복해서 추가한다
    step7 = step6[:]
    
    while len(step7) < 3:
        step7 += step6[-1]
    
    
    
    return step7