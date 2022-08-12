# [4673] 셀프 넘버
def d(n):
    n += sum(map(int, str(n)))
    return n


noSelfNumber = set()

for i in range(1, 10001):
    noSelfNumber.add(d(i))
for i in range(1, 10001):
    if i not in noSelfNumber:
        print(i)
