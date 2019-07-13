x = input("enter your email address: ")
x = x.split("@")
company = x[1].split(".")
print(company[0])
