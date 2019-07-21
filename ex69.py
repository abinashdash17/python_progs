import re
x = input("Enter an expression: ")
operand = re.findall(r'\d+',x)
operator = re.findall(r'\D',x)
if operator[0] == '+':
    res = int(operand[0]) + int(operand[1])
if operator[0] == '-':
    res = int(operand[0])- int(operand[1])
if operator[0] == '*':
    res = int(operand[0])* int(operand[1])
if operator[0] == '/':
    res = int(operand[0]) / int(operand[1])
print(res)
