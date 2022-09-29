# 총 다섯 개 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 
# 구분되어 주어진다. 가장 많은 점수를 얻은 사람이 우승한다.
# 첫째 줄에 우승자의 번호와 그가 얻은 점수를 출력한다.

scores = [0, 0, 0, 0, 0] # 각 요리사의 총점을 저장할 리스트

for i in range(5): # 5명의 점수를 받는다.
    scores[i] = sum(map(int, input().split()))
max_score = max(scores) # 총점 중 제일 큰 점수를 찾는다.
print(scores.index(max_score) + 1, max_score) # 제일 큰 점수의 요리사와, 점수를 출력한다.