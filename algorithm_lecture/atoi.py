# 숫자를 하나씩 잘라서 그 숫자에 해당하는 문자열로 만들어 반환함
def atoi(string):
    n = 1
    result = 0
    for s in string:
        result += (ord(s) - 48) * (10 ** (len(string) - n))
        n += 1
    print(type(result))


def itoa(num):
    n_lst = []
    while num >= 1:
        s = num % 10
        n_lst.insert(0, chr(s + 48))
        num //= 10 
    print(type(''.join(n_lst)))


atoi('243')
itoa(243)