def decora(func):
    def p(x):
        print("Hello There!")
        func(x)
        print("Welcome to python classes")
    return p
@decora
def ecname(x):
    print(x)

x = input("enter your name: ")
ecname(x)
