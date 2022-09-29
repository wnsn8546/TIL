# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
# 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
# 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다.
# 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.

T = int(input()) # 테스트케이스 개수를 입력 받는다.

for test_case in range(1, T+1): # T만큼 반복한다.
    PS = input() # 괄호 문자열을 입력받는다.
    if PS[0] == ')': # 만약 시작이 ')'라면,
        print('NO') # 'NO'를 출력하고 다음 케이스로 넘어간다.
        continue

    stack = [] # 스택으로 사용할 리스트
    for i in PS: # 문자열을 순회하면서
        if i == '(': # 여는 괄호를 만나면
            stack.append(i) # stack에 넣어준다.
        else:               # 여는괄호가 아니면 = 닫는괄호이면
            if len(stack):  # 스택이 남아있다면
                stack.pop() # pop을 해준다.
            else:           # 스택이 비어있다면
                print('NO') # 'NO를 출력하고 반복문을 종료한다.
                break
    else: # break를 하지않고 for문을 다 돌았을때,
        if len(stack): # stack이 남아있다면
            print('NO') # 'NO'
        else:
            print('YES') # 'YES'