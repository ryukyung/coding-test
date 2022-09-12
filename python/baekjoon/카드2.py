# [1460] 카드2
from collections import deque
n = int(input())
queue = deque([i for i in range(1, n+1)])

while len(queue) > 1:
    queue.popleft()
    moveCard = queue.popleft()
    queue.append(moveCard)
print(queue[0])