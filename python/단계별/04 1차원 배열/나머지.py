# [3052] 나머지
# 집합 자료형(set): 중복 허용X, 순서 없음
divideList = []
for _ in range(10):
    number = int(input())
    divideList.append(number % 42)
divideList = set(divideList)
print(len(divideList))
