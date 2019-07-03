x = input("Enter a sentence: ")
y = x.split(" ")
y_set = set(y)
wc = {}
for word in y_set :
    count = 0
    for item in y :
        if word == item :
            count += 1
    wc[word] = count
for word in sorted(y_set) :
    print("{} : {}".format(word,wc[word]))
