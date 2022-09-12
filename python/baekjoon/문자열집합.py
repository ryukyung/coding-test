# [14425] 문자열 집합
n, m = map(int, input().split())
sSet = set([input() for _ in range(n)])
result = 0 
for _ in range(m):
    check = input()
    if check in sSet:
        result += 1 
print(result)