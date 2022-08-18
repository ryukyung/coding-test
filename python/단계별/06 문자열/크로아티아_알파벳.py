# [2941] 크로아티아 알파벳
alphabet = ["c=", "c-", "dz=", "d-", "lj",  "nj", "s=", "z="]
croatia = input()
for i in alphabet:
    croatia = croatia.replace(i, '*')
print(len(croatia))
