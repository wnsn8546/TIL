# https://www.acmicpc.net/problem/2941

word = input()
croatia_list = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳 리스트

for char in croatia_list: # 크로아티아 알파벳과 일치하는 문자들을 '!'로 바꿔준다.
    word = word.replace(char, '!')
print(len(word)) # for문을 통과한 word의 전체길이를 출력한다.