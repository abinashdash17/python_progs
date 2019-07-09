def f(a):
    def g(b):
        return a**b
    return g

base = f(2)
power=base(10)
print(power)
