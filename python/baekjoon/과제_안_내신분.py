# [5597] 과제 안 내신 분..?
studentNumber = [i for i in range(1, 31)]
for _ in range(28):
    number = int(input())
    studentNumber.remove(number)
print(min(studentNumber))
print(max(studentNumber))
