def foo(func):
    def pr(x):
        print(func(x))
    return pr
@foo
def sq(x):
    return x**2
sq(5)
