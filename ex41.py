def halfs():
    li = [i for i in range(1,11)]
    l = len(li) / 2
    print(li[:int(l)])
    print(li[int(l):])

halfs()
