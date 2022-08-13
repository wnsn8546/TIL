N = int(input())

for count in range(1, N + 1):
    for blank in range(N - count):
        print(' ', end='')
    for star in range(count):
        print('*', end='')
    print()