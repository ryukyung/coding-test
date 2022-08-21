# [12948] 핸드폰 번호 가리기
def solution(phone_number):
    answer = '*' * (len(phone_number)-4)
    answer += phone_number[-4:]
    return answer
