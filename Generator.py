# def gener1():
#     yield 10
#     yield 20
#     yield 30
#     yield 40
# num=gener1()

# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))


def gener1():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50
num=gener1()    
for i in num:
    print(i)