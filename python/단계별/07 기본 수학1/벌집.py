# [2292] 벌집
room = int(input())
honeycombCount = 1
result = 1
while room > honeycombCount:
    honeycombCount += 6 * result
    result += 1
print(result)
