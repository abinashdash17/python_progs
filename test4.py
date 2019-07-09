def g():
    print("it's me 'g'")
    print("Thanks for calling me.")

def f(func):
    print("hi, it's me 'f'")
    print("I will call {} now".format(func.__name__))
    func()

f(g)
