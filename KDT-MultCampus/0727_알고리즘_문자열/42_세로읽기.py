# https://www.acmicpc.net/problem/10798

word_list = [] # 단어들을 저장할 리스트변수
length_list = [] # 단어들의 길이를 저장할 리스트 변수
result = '' # 세로읽기 결과를 담을 변수

for i in range(5): # 5개의 단어를 받고, 각 리스트에 단어와 단어의 길이를 추가한다.
    word = input()
    word_list.append(word)
    length_list.append(len(word))
    
for i in range(max(length_list)): # 제일 긴 단어의 길이만큼 순회하고,
    for j in range(5): # 단어의 개수만큼 순회한다.
        if i < length_list[j]: # 현재 단어의 길이를 넘지 않는경우에 세로로 문자를 합쳐나아간다.
            result += word_list[j][i] 
print(result)