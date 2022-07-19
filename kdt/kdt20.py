# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
# Input 123
# Output 6

n = input()
result = 0

for i in n:
    result += int(i)
    
print(result)