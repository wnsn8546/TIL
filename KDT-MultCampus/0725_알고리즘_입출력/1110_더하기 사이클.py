N = input()
if int(N) < 10:
    N = '0' + N
    
old_number = N
new_number = '0'
sum_number = '0'
count = 0

while True:
    if N == str(new_number):
        break
    sum_number =  str(int(old_number[0]) + int(old_number[1]))
    new_number = old_number[-1] + sum_number[-1]
    
    count += 1
    old_number = new_number
print(count)