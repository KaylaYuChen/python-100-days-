import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level = characters in order
easy_password = ""
for char in range(nr_letters):
    easy_password += random.choice(letters)
for char in range(nr_symbols):
    easy_password += random.choice(symbols)
for char in range(nr_numbers):
    easy_password += random.choice(numbers)

print(f"Your new password is : {easy_password}")

# Hard Level = characters shuffled
password_list = []
for char in range(nr_letters):
    password_list.append(random.choice(letters))
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

print(f"Unshuffled list: {password_list}")

random.shuffle(password_list)
print(f"Shuffled list: {password_list}")

hard_password = ""
for char in password_list:
    hard_password += char

print(f"Your new password is: {hard_password}")
