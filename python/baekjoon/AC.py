# [5430] AC
import sys 
from collections import deque 
input = sys.stdin.readline
testCase = int(input())
for i in range(testCase):
    p = input().strip()
    nCount = int(input())
    nList = input().strip()
    queue = deque(nList[1:-1].split(','))
    reverseCount = 0 
    temp = 1 

    if nCount == 0:
        queue = deque()
    
    for i in range(len(p)):
        if p[i] == 'R':
            reverseCount += 1 
        elif p[i] == 'D':
            if len(queue) == 0:
                print('error')
                temp = 0 
                break 
            else:
                if reverseCount %2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if temp == 0:
        continue
    else:
        if reverseCount %2 == 0:
            print(f'[{",".join(queue)}]')
        else:
            queue.reverse()
            print(f'[{",".join(queue)}]')