# https://www.acmicpc.net/problem/1157

word = input().upper() # 단어를 받고 대문자로 변환한뒤 저장한다.
my_dict = {} # 개수를 판단하기 위한 딕셔너리를 선언, 초기화한다.

for char in word: # for문으로 순회하면서 딕셔너리에 value값을 더해준다.
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1

max_alpabet = max(my_dict, key = my_dict.get) # 제일 큰 value의 알파벳을 구한다.
cnt = 0 # 제일 큰 value를 가진 알파벳을 카운트하기위한 변수
for i in my_dict: # for문으로 순회하면서 제일 큰 value와 같은 개수를 더한다.
    if my_dict[i] == my_dict[max_alpabet]:
        cnt +=1 
        
if cnt == 1: # 1개일때는 제일 큰 value를 가진 알파벳을 출력하고, 그렇지않을때는 '?'를 출력한다.
    print(max_alpabet)
else:
    print('?')