import random
import string

# Define sets of characters to choose from
letters = string.ascii_letters  # Includes both uppercase and lowercase letters
numbers = string.digits  # Includes digits 0-9
symbols = string.punctuation  # Includes various punctuation symbols

# Ask the user how many characters of each type they want in the password
no_of_letters = int(input("\nHow many letters do you want in your password? "))
no_of_numbers = int(input("How many numbers do you want in your password? "))
no_of_symbols = int(input("How many symbols do you want in your password? "))

password = ""  # Initialize an empty string to store the password

# Generate the password by randomly selecting characters from each set
for i in range(1, no_of_letters + 1):
    password += random.choice(letters)

for i in range(1, no_of_numbers + 1):
    password += random.choice(numbers)

for i in range(1, no_of_symbols + 1):
    password += random.choice(symbols)

# Convert the password string to a list and shuffle the characters randomly
final_password = list(password)
random.shuffle(final_password)

# Convert the shuffled list back to a string to get the final password
final_password = "".join(final_password)

# Display the suggested password to the user
print("\nYour suggested password is: " + final_password)
