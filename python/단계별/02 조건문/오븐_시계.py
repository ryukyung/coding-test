# [2525] 오븐 시계
hour, minute = map(int, input().split())
spendMinute = int(input())

hour += spendMinute//60
minute += spendMinute % 60
if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24
print(hour, minute)
