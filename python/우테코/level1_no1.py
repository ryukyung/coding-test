import math


def calcMaxPage(page):
    pageNumber = [page//100, (page % 100) // 10, (page % 100) % 10]
    if 0 in pageNumber:
        pageNumber.remove(0)
    add = sum(pageNumber)
    mul = math.prod(pageNumber)
    return add, mul


def problem1(pobi, crong):
    answer = 0

    if pobi[0] + 1 == pobi[1] and crong[0] + 1 == crong[1] and pobi[0] % 2 != 0 and pobi[1] % 2 == 0 and crong[
            0] % 2 != 0 and crong[1] % 2 == 0:

        # pobi
        pobiLeft = calcMaxPage(pobi[0])
        pobiRight = calcMaxPage(pobi[1])

        crongLeft = calcMaxPage(crong[0])
        crongRight = calcMaxPage(crong[1])
        pobiList = [pobiLeft[0], pobiLeft[1], pobiRight[0], pobiRight[1]]
        crongList = [crongLeft[0], crongLeft[1], crongRight[0], crongRight[1]]

        pobiMax = max(pobiList)
        crongMax = max(crongList)
        # print(pobiMax)
        # print(crongMax)
        # 4. 비교하기 -> 0, 1, 2
        if pobiMax > crongMax:
            answer = 1
        elif pobiMax < crongMax:
            answer = 2
        elif pobiMax == crongMax:
            answer = 0
    else:
        answer = -1
    return answer
