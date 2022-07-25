# [12919] 서울에서 김서방 찾기
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            result = i
    # return('김서방은 ' + str(result) + '에 있다')
    return(f'김서방은 {result}에 있다')
