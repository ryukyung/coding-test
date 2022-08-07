# [25304] 영수증
totalAmount = int(input())
buyCount = int(input())
for i in range(buyCount):
    amount, count = map(int, input().split())
    totalAmount -= (amount*count)
if totalAmount == 0:
    print("Yes")
else:
    print("No")
