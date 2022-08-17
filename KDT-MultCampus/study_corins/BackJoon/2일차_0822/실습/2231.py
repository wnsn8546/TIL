# 자연수 N이 주어졌을때, N의 가장 작은 생성자를 구하기.

N = int(input()) # N을 입력 받는다.

for i in range(1, N+1): # i를 1부터 N까지 순회한다.
    temp = i # temp = i + i의 각 숫자를 만들기위해 temp를 i값으로 매번 초기화한다.
    for j in str(i): # i를 str로 형변환하고 각 숫자들을 j로 뽑아낸다.
        temp += int(j) # 초기값인 i 와 각 자리수를 더한다.
    if temp == N: # 더한값이 N과 같으면 생성자이므로, 
        print(i) # i를 출력하고 break해준다.
        break
    if i == N: # 만약 i가 N까지 왔으면 0을 출력해준다.
        print(0)