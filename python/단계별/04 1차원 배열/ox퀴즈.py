# [8958] OX 퀴즈
testCase = int(input())
for _ in range(testCase):
    oxList = list(input())
    score = 0
    result = 0
    for i in oxList:
        if i == 'O':
            score += 1
            result += score
        else:
            score = 0
    print(result)
