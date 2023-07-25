import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

no_of_letters = int(input("\nHow many letters do you want in your password? "))
no_of_numbers = int(input("How many numbers do you want in your password? "))
no_of_symbols = int(input("How many symbols do you want in your password? "))

password = ""

for i in range(1, no_of_letters + 1):
    password += random.choice(letters)

for i in range(1, no_of_numbers + 1):
    password += random.choice(numbers)

for i in range(1, no_of_symbols + 1):
    password += random.choice(symbols)

final_password = list(password)
random.shuffle(final_password)
final_password = "".join(final_password)

print("\nYour suggested password is: " + final_password)
