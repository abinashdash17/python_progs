x = input("Enter words to be sorted:")
str_list = x.split(',')
str_list.sort()
str1 = ','.join(str_list)
print(str1)