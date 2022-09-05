# 단어공부 https://www.acmicpc.net/problem/1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

word = input().upper()

alpahbet_dict = {}
for i in range(len(word)):
    if word[i] in alpahbet_dict:
        alpahbet_dict[word[i]] += 1
    else:
        alpahbet_dict[word[i]] = 1
max_num_alphabet = max(alpahbet_dict.values())

max_num_alphabet_list = []
for k, v in alpahbet_dict.items():
    if alpahbet_dict[k] == max_num_alphabet:
        max_num_alphabet_list.append(k)

if len(max_num_alphabet_list) != 1:
    print('?')
else:
    print(max_num_alphabet_list[0])