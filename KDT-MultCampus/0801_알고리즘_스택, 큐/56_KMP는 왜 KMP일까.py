# https://www.acmicpc.net/problem/2902

long_list = list(map(str, input().split('-')))
result = ''
# input을 받을때 split으로 '-'을 기준으로 나눠서 리스트에 담은 뒤,
# 첫번째 문자만을[0]로 가져와 붙여서 출력한다.
for i in long_list:
    result += i[0]
print(result)