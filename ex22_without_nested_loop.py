x = input("Enter a sentence")
x = x.split(" ")
wc = {}
for word in set(x):
    wc[word] = 0
for word in x :
    wc[word] += 1
for i in sorted(wc.keys()) :
    print("{} : {} ".format(i,wc[i]))
