def solution(my_string):
    total = 0
    for ch in my_string:
        if ch.isdigit():      # 문자가 숫자인 경우
            total += int(ch)  # 정수로 변환 후 합산
    return total