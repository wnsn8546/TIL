# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
# Input banana
# Output
# b 1
# a 3
# n 2

word = input()
my_dict = {}

for i in word:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

for k,v in my_dict.items():
    print(k, v)