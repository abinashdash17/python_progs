import random
x = random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5)
print(x)
