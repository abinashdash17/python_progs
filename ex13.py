x = input("Enter a sentence:")
no_of_alpha = 0
no_of_digit = 0
for ch in x:
    for i in range(65,90):
        if ch == chr(i) :
            no_of_alpha = no_of_alpha + 1
    for i in range(97,122):
        if ch == chr(i) :
            no_of_alpha = no_of_alpha + 1
    for i in range(48,57):
        if ch == chr(i) :
            no_of_digit = no_of_digit + 1
print("LETTERS {}".format(no_of_alpha))
print("DIGITS {}".format(no_of_digit))

