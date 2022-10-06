K = int(input())

for _ in range(K):
    scores = list(map(int, input().split()))
    student_num = scores[0]
    scores.pop(0)
    max_score = max(scores)
    min_score = min(scores)
    scores = sorted(scores, reverse = True)
    
    largest_gap = 0
    for i in range(len(scores) - 1):
        if scores[i] - scores[i+1] > largest_gap:
            largest_gap = scores[i] - scores[i+1]

    print(f'Class {_ + 1}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {largest_gap}')