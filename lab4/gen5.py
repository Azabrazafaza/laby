n = int(input())
def gen(a):
    while a != -1:
        yield a
        a -= 1
answer = gen(n)
while n != 0:
    print(next(answer))