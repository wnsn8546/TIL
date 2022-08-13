# https://www.acmicpc.net/problem/2711

T = int(input()) # 전체 개수
location = '' # 단어에서 지워야할 문자의 위치
word = '' # 단어
result = [] # 결과들을 저장할 리스트

for i in range(T): # 전체 단어 개수만큼 돌면서, location, word값과 result리스트길이를 저장한다.
    location, word = input().split()
    result.append('')
    # 단어의 길이만큼 단어의 문자를 돌면서 location위치의 문자만빼고 result에 넣어준다
    for j in range(0, len(word)):
        if j == int(location)-1:
            continue
        else:
            result[i] += word[j]

for i in result:
    print(i)