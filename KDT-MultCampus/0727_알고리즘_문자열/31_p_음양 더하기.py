# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    # for문으로 순회하면서 singns[i]가 참이면 answer에 더하기, 거짓이면 빼준다
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
        
    return answer

# absolutes = [4, 7, 12]
# signs = [True, False, True]
# print(solution(absolutes, signs))

# absolutes = [1, 2, 3]
# signs = [False, False, True]
# print(solution(absolutes, signs))