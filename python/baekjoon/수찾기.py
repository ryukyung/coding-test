# [1920] 수 찾기
import sys
input = sys.stdin.readline
n = int(input())
nList = set(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

""" 
result = []
for i in mList:
    if i in nList:
        temp = 1
    else:
        temp = 0
    result.append(temp)
print(*result, sep='\n') 
"""

print(*[1 if i in nList else 0 for i in mList], sep='\n')