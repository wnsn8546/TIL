# 첫째 줄에 N과 X를 입력받는다.
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다.
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다.

N, X = map(int, input().split()) # N과 X를 입력받는다.
A = list(map(int, input().split())) # 공백을 기준으로 정수 N개를 받고 리스트로 만든다.

for i in range(len(A)): # A의 길이만큼 i를 0부터 순회한다.
    if A[i] < X:             # A[i]의 숫자가 X보다 작으면,
        print(A[i], end=' ') # 공백으로 구분해 출력한다.