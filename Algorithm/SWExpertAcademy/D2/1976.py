T = int(input())

for test_case in range(1, T + 1):
    t1, m1, t2, m2 = map(int, input().split())
    
    t = 12 if (((t1 + t2) + (m1 + m2) // 60) % 12) == 0 else (((t1 + t2) + (m1 + m2) // 60) % 12)
    m = (m1 + m2) % 60

    print(f'#{test_case}', t, m)