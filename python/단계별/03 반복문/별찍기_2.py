# [2439] 별찍기-2
starNumber = int(input())
for i in range(1, starNumber+1):
    print(' '*(starNumber-i)+'*'*i)
