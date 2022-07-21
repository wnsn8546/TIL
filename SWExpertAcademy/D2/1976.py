T = int(input())

for test_case in range(1, T + 1):
    t1, m1, t2, m2 = map(int, input().split())

    if (t1 + t2) >= 12 and (m1 + m2) >= 60:
        print(f'#{test_case}', (t1 + t2 + 1) - 12,  (m1 + m2) - 60)
    elif (t1 + t2) >= 12:
        print(f'#{test_case}', (t1 + t2) - 12, m1 + m2)
    elif (m1 + m2) >= 60 :
        print(f'#{test_case}', (t1 + t2) + 1, (m1 + m2) - 60)
    else:
        print(f'#{test_case}', t1 + t2, m1 + m2)