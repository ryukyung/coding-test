# [1546] 평균
countSubject = int(input())
scoreList = int(input().split())
avgList = []
for i in scoreList:
    avgList.append(i/max(scoreList)*100)
print(sum(avgList)/countSubject)
