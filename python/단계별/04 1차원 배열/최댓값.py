# [2562] 최댓값
numbers = []
for _ in range(9):
    numbers.append(int(input()))
print(max(numbers))
print(numbers.index(max(numbers))+1)
