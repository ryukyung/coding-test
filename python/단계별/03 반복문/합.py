# [8393] 합
# 방법1
number = int(input())
print(sum(range(1, number+1)))

# 방법2
print(sum(range(1, int(input())+1)))

# 방법3
number = int(input())
sumResult = 0
for i in range(1, number+1):
    sumResult += i
