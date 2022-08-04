# [11021] A+B-7
testCase = int(input())
for i in range(1, testCase+1):
    number1, number2 = map(int, input().split())
    print(f'Case #{i}: {number1+number2}')
    print('Case #{}: {}'.format(i, number1+number2))
