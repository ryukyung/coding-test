# [10952] A+B-5
while True:
    number1, number2 = map(int, input().split())
    if number1 == 0 and number2 == 0:
        break
    else:
        print(number1+number2)
