def solution(num, k):
    answer = 0
    k = str(k)
    num = str(num)
    if k in num:
        answer = num.index(k) + 1
    else:
        answer = -1
    return answer