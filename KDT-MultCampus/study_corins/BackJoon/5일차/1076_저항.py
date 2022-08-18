# 처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다.
# 첫째 줄에 첫 번째 색, 둘째 줄에 두 번째 색, 셋째 줄에 세 번째 색이 주어진다.
# 입력으로 주어진 저항의 저항값을 계산하여 첫째 줄에 출력한다.

resistor_dict = { # 저항값들의 딕셔너리를 만들어 놓는다. 
    'black': ['0', 1],
    'brown': ['1', 10],
    'red': ['2', 100],
    'orange': ['3', 1000],
    'yellow': ['4', 10000],
    'green': ['5', 100000],
    'blue': ['6', 1000000],
    'violet': ['7', 10000000],
    'grey': ['8', 100000000],
    'white': ['9', 1000000000]
} # 값에 해당하는 부분은 더하기 좋게 문자열로 만들어 놓는다. 

first = input() # 세개의 색을 입력 받는다.
second = input()
third = input()
# 출력한다.
print(int(resistor_dict[first][0] + resistor_dict[second][0]) * int(resistor_dict[third][1]))