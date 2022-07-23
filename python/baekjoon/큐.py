# [10846] 큐
import sys
queueList = []
chance = sys.stdin.readline()
for _ in range(int(chance)):
    inputList = sys.stdin.readline().split()
    if inputList[0] == 'push':
        queueList.append(inputList[1])
    elif inputList[0] == 'pop':
        if queueList:
            print(queueList.pop(0))
        else:
            print(-1)
    elif inputList[0] == 'size':
        print(len(queueList))
    elif inputList[0] == 'empty':
        if len(queueList) == 0:
            print(1)
        else:
            print(0)
    elif inputList[0] == 'front':
        if queueList:
            print(queueList[0])
        else:
            print(-1)
    elif inputList[0] == 'back':
        if queueList:
            print(queueList[-1])
        else:
            print(-1)
