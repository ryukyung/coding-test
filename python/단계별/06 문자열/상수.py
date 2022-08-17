# [2908] 상수
number1, number2 = input().split()
number1, number2 = int(number1[::-1]), int(number2[::-1])
if number1 > number2:
    print(number1)
else:
    print(number2)