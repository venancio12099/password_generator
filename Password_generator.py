import random

print("Welcome password generator")

#Error message if the input is an empty space, str or 0.
def ask_int(prompt):
    while True:
        value = input(prompt).strip()

        if not value.isdigit():
            print("ERROR, please indicate the lenght of your passworda")
            continue

        value = int(value)

        if value <= 5:
           print("ERROR, password must have a minimum lenght of 6")
           continue

        return value
        
length = ask_int("Please introduce the desired password lenght: ")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@$%&*().,?0123456789"

print("Find your password below: ")

password = ""

for pwd in range(length):
    password += random.choice(chars)

print(password)
