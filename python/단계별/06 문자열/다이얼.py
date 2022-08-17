# [5622] 다이얼
phoneNumber = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
call = list(input())
time = 0
for i in call:
    for j in phoneNumber:
        if i in j:
            time += phoneNumber.index(j)+3
print(time)
