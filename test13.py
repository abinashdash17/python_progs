if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

l1 = list(arr)
ls = sorted(l1)
i = -1
while True:
    if ls[-1] != ls[i]:
        run_up = ls[i]
        break
    elif i == -len(ls):
        run_up = 'none'
        break
    i-=1
print(run_up)
