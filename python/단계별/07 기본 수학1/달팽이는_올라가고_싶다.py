# [2869] 달팽이는 올라가고 싶다
# python, pypy -  시간초과
a, b, v = map(int, input().split())
day = 0
height = 0
while True:
    day += 1
    if a*day-b*(day-1) >= v:
        break
print(day)

# 정답
a, b, v = map(int, input().split())
day = (v-b)/(a-b)
if day == int(day):
    print(int(day))
else:
    print(int(day)+1)
