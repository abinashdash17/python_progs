x = input("Enter a sentence")
x = x.split(" ")
wc = {}
for word in x :
    wc[word] = wc.get(word,0) + 1
for i in sorted(wc.keys()) :
    print("{} : {} ".format(i,wc[i]))
