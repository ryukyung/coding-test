# [1065] 한수
# for문
n = int(input())
result = 0
for i in range(1, n+1):
    if i < 100:
        result += 1
    else:
        nStrList = list(map(int, str(i)))
        if nStrList[0] - nStrList[1] == nStrList[1] - nStrList[2]:
            result += 1
print(result)

# 함수


def findHansu(number):
    result = 0
    for i in range(1, number+1):
        numberStrList = list(map(int, str(i)))
        if i < 100:
            result += 1
        elif numberStrList[0] - numberStrList[1] == numberStrList[1] - numberStrList[2]:
            result += 1
    return result


number = int(input())
print(findHansu(number))
