# [1316] 그룹 단어 체커
countWord = int(input())
result = countWord
for i in range(countWord):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result -= 1
            break
print(result)
