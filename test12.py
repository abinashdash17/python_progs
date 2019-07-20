import re
def is_valid_card(str1):
    str2 = ''.join(re.findall(r'\d',str1))
    pat1 = r"^[456]"
    pat2 = "\d"
    pat3 = r'\d{4}-?\d{4}-?\d{4}-?\d{4}'
    pat4 = r'(\d)\1{3,16}'
    a = b = c = d = False
    if  re.match(pat1,str1):
        a = True
    if  len(re.findall(pat2,str1))== 16 :
        b = True
    if  re.match(pat3,str1):
        c = True
    if len(re.findall(pat4,str2)) == 0:
        d = True
    if a & b & c & d :
        return True
    else :
        return False
n = int(input("Enter N: "))
l1 = []
for i in range(0,n):
    str1 = input()
    l1.append(str1)
for str1 in l1:
    if is_valid_card(str1):
        print("Valid")
    else :
        print("Invalid")
