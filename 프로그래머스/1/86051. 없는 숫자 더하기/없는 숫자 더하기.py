def solution(numbers):
    answer = 0
    arr = []
    for i in range(0, 10, 1):
        if i in numbers:
            pass
        else:
            arr.append(i)
            
        answer = sum(arr)
    return answer