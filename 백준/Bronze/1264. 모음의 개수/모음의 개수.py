vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    input_str = input()
    cnt = 0

    if '#' in input_str:
        break
    else:
        for i in input_str:
            if i in vowel_list:
                cnt +=1
    print(cnt)