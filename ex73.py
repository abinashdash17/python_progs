import random
while(input()):
  x = random.choice([i for i in range(0,211) if (i%5 == 0 and i%7==0)])
  print(x)
