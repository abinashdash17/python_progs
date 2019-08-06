import timeit
stm = '[i for i in range(0,100)]'
print(timeit.timeit(stm,number=500))
