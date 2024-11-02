x = 1

def foo():
    global x
    x = 2

    def bar():
        x = 3
        print(x)

    bar()
    print(x)

foo()
print(x)

