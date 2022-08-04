# [1110] 더하기 사이클
firstNumber = int(input())
number = firstNumber
count = 0
while True:
    ten = number//10
    one = number % 10
    otherNumber = (ten + one) % 10
    number = (one*10) + otherNumber

    count += 1
    if firstNumber == number:
        break
print(count)
