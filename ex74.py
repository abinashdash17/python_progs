import random
l = []
for i in range(5):
    l.append(str(random.choice([j for j in range(100,201)])))
print(",".join(l))
