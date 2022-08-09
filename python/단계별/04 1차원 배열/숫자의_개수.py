# [2577] 숫자의 개수
number1 = int(input())
number2 = int(input())
number3 = int(input())
result = list(str(number1*number2*number3))

for i in range(10):
    print(result.count(str(i)))
