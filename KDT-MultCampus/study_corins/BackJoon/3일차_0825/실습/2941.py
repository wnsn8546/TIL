# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# 알파벳 소문자와 '-', '='로만 이루어져 있다.

croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = str(input()) # 주어진 단어를 입력받는다.

for i in croatia_list: # croatia_list를 순회한다.
    word = word.replace(i, '!') # word에 해당 문자가 있으면 '!'로 바꿔준다.
print(len(word)) # 바뀐 word의 문자 길이를 출력한다.