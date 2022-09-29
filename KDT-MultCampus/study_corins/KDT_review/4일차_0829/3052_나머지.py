# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다.
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

my_dict = {} # 나머지들을 담아 놓을 딕셔너리를 만들어 놓는다.

for _ in range(10): # 10번 입력을 받는다.
    num = int(input())
    remainder = num % 42 # remainder에 나머지 값을 저장해 놓는다.

    if remainder not in my_dict: # 해당하는 나머지가 my_dict에 없었으면 1
        my_dict[remainder] = 1
    else:
        my_dict[remainder] += 1 # 있었으면 += 1 을 해준다.
print(len(my_dict)) # 서로다른 나머지 개수인 딕셔너리의 길이를 출력한다.