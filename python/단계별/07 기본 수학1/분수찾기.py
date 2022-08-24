# [1193] 분수찾기
x = int(input())

line = 0
maxNum = 0
while x > maxNum:
    line += 1
    maxNum += line

temp = maxNum - x
if line % 2 == 0:
    top = line-temp
    bottom = temp+1
else:
    top = temp + 1
    bottom = line-temp
print(f'{top}/{bottom}')
