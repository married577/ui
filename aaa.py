a = ''


def fun():
    global a
    a = 3


fun()
print(a)


def fun1():
    global a
    a = 5


fun1()
print(a)


