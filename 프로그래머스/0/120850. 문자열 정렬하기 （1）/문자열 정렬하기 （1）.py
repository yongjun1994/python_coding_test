def solution(my_string):
    numbers = []
    for ch in my_string:
        if '0' <= ch <= '9': 
            numbers.append(int(ch))
    numbers.sort()
    return numbers

