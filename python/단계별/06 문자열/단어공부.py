# [1157] 단어 공부
word = input().upper()
wordList = list(set(word))
countList = []
for i in wordList:
    count = word.count(i)
    countList.append(count)

if countList.count(max(countList)) > 1:
    print('?')
else:
    maxIndex = countList.index(max(countList))
    print(wordList[maxIndex])
