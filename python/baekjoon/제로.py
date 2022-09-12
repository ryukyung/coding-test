# [10773] 제로
k = int(input())
numberList = [] 
for i in range(k):
    number = int(input())
    if number == 0:
        numberList.pop()
    else:
        numberList.append(number)

print(sum(numberList))