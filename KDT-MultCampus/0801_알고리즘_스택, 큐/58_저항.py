# https://www.acmicpc.net/problem/1076

resistor_dict = { # 저항정보를 담은 딕셔너리
    'black': [0, 1],
    'brown': [1,10],
    'red': [2, 100],
    'orange': [3, 1000],
    'yellow': [4, 10000],
    'green': [5, 100000],
    'blue': [6, 1000000],
    'violet': [7, 10000000],
    'grey': [8, 100000000],
    'white': [9, 1000000000]
    }
result = '' # 결과를 담을 변수

for i in range(1, 4): # 3번을 돌고, 1,2번째는 값을 더하고 3번째는 곱한다.
    resistor = input()
    if i < 3:
        result += str(resistor_dict[resistor][0])
    else:
        result = int(result) * resistor_dict[resistor][1]
print(result)