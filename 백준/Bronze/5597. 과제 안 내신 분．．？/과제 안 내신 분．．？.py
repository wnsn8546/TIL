student_list = [0] * 30
for i in range(28):
    N = int(input())
    student_list[N-1] += 1
for i in range(30):
    if student_list[i] != 1:
        print(i+1)