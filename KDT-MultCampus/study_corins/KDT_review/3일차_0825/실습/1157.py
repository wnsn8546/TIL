# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 출력하라.
# 단 대소문자 구분은 하지않고, 가장많은 알파벳이 여러개면 '?'을 출력.

word = input().upper() # 입력받은 단어를 먼저 대문자로 바꿔준다.
my_dict = {} # 알파벳의 빈도수를 담을 딕셔너리를 만든다.

for i in word: # 단어의 알파벳들을 순회한다.
    if i not in my_dict: # 딕셔너리에 없던 알파벳이면 값을 1로 해서 추가한다.
        my_dict[i] = 1
    else:                # 있던 알파벳이면 값에 +1을 해준다.
        my_dict[i] += 1
max_alphabet = max(my_dict.values()) # 빈도수 중 제일 큰 값을 찾는다.

cnt = 0 # 최대빈도수와 같은 알파벳이 몇개인지 카운트하기위한 변수
for k, v in my_dict.items(): # k, v 값들을 순회한다. 
    if v == max_alphabet: # max값과 같은 값을 찾으면,
        alphabet = k    # 해당하는 알파벳을 저장하고,
        cnt += 1        # cnt를 +1 해준다.
    if cnt == 2: # 2개째 찾았을 경우
        print('?') # '?'를 출력하고 break로 반복문을 종료한다.
        break
if cnt == 1: # 한 개만 있었을 경우, 해당 알파벳을 출력한다.
    print(alphabet)