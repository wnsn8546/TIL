# https://www.acmicpc.net/problem/2789

cam_word = 'CAMBRIDGE'
word = input()

for char in word: # for문을 순회하면서 'CAMBRIDGE' 에 포함된 알파벳과 같은것은 공백으로 바꿔준다.
    if char in cam_word:
        word = word.replace(char, '')
print(word)