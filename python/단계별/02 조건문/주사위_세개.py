# [2480] 주사위 세개
one, two, three = map(int, input().split())
if one == two == three:
    print(10000 + one * 1000)
elif (one == two) or (one == three):
    print(1000 + one * 100)
elif two == three:
    print(1000 + two * 100)
else:
    print(100 * max(one, two, three))
