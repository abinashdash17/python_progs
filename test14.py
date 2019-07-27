def r(x):
    if x>1:
        return r(x-1)
    else:
        return 1

print(r(9))
