# [1929] 소수 구하기
startNumber, endNumber = map(int, input().split())
for i in range(startNumber, endNumber+1):
    if i <= 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)
