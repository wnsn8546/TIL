N = int(input())

for line in range(1, N + 1):
    if line % 2 == 0 :
        for count in range(N):
            print(' *', end='')
    else:
        for count in range(N):
            print('* ',  end='')
    print()