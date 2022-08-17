# sings[i]가 True이면 answer에 더하고, 
# False이면 answer에서 뺀다.


def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)): # absolutes의 길이만큼 순회한다.
        if signs[i]: # sings[i]가 True이면 answer에 더하고,
            answer += absolutes[i]
        else:        # False이면 answer에서 뺀다.
            answer -= absolutes[i]
        
    return answer # 답을 리턴한다.