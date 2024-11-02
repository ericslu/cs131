x = 1

def foo():
    x = 2

    def bar():
        nonlocal x
        x = 3
        print(x)

    bar()
    print(x)

foo()
print(x)

