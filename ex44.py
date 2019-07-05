def even_odd(x):
    if x % 2 == 0 :
        return True
    else :
        return False
li = [ i for i in range(1,11) ]
filter_obj = filter(even_odd,li)
print(list(filter_obj))
