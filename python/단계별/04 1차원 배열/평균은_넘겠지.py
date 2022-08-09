# [4344] 평균은 넘겠지
testCase = int(input())
for _ in range(testCase):
    numberList = list(map(int, input().split()))
    scoreAvg = sum(numberList[1:])/numberList[0]
    count = 0
    for i in numberList[1:]:
        if i > scoreAvg:
            count += 1
    result = (count/numberList[0]) * 100
    # print(f'{round(result,3)}%')
    print(f'{result:.3f}%')
