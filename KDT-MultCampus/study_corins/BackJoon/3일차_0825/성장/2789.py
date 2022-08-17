# 첫째 줄에  알파벳 대문자로 이루어진 단어가 주어진다.
# CAMBRIDGE에 포함된 알파벳을 모두 지운 뒤 출력한다.

word = input() # 단어를 입력받는다.

for i in word: # 단어의 알파벳들을 순회한다.
    if i not in 'CAMBRIDGE': # i가 'CAMBRIDGE'에 속하지 않는 알파벳이면,
        print(i, end='') # 공백없이 이어서 하나씩 출력해준다.