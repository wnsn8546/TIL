# 학점은 상대평가로 주어지는데, 총 10개의 평점이 있다.
# A+, A0, A-, B+, B0, B-, C+, C0, C-, D0
# 총점 = 중간고사(35%) + 기말고사(45%) + 과제(20%)
# 10 개의 평점을 총점이 높은 순서대로 부여하는데,
# 각각의 평점은 같은 비율로 부여할 수 있다.
# N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.
# 입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,
# 학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
# K 번째 학생의 학점을 출력하는 프로그램을 작성하라.
import sys
sys.stdin = open("input.txt", "r")

grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input()) # 테스트 케이스 T.

for test_case in range(1, T+1): # T만큼 반복.
    N, K = map(int, input().split()) # 학생 수N, 학점을 알고싶은 학생의 번호K
    total_score_list = [] # 배점을 계산한 총점들을 저장할 리스트
    K_score = 0 # 찾을 번호의 학생의 점수
    num_per_grade = N // 10 # 점수당 인원 수

    for i in range(N): # N번 반복하면서
        mid_term, final_term, assignment = map(int, input().split()) # 중간, 기말, 과제 점수를 입력받고
        total_score = (mid_term * 0.35) + (final_term * 0.45) + (assignment * 0.20) # 총점을 계산.
        total_score_list.append(total_score) # 리스트에 추가한다.
        
        if i == (K-1): # K번째의 점수를 찾고,
            K_score = total_score # 저장해준다.
    total_score_list = sorted(total_score_list, reverse= True) # 내림차순 정렬을하고
    
    grade = total_score_list.index(K_score) // num_per_grade # 몇번째 점수에 해당할지를 저장하고
    print(f'#{test_case} {grade_list[grade]}') # 출력한다.