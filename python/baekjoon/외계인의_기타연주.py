# [2841] 외계인의 기타 연주
import sys 
n, p = map(int, sys.stdin.readline().split())
lineTable = [[0] for _ in range(7)]
result = 0

for i in range(n):
    lineNumber, pNumber = map(int, sys.stdin.readline().split())
    while lineTable[lineNumber][-1] > pNumber:
        lineTable[lineNumber].pop()
        result += 1 
    if lineTable[lineNumber][-1] == pNumber:
        continue
    lineTable[lineNumber].append(pNumber)
    result += 1 


print(result)