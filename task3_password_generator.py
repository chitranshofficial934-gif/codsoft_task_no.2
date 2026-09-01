# CODSOFT Python Programming Internship
# Task 3: Password Generator

import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("================================")
print("       PASSWORD GENERATOR")
print("================================")

while True:

    try:
        length = int(input("\nEnter password length: "))

        if length <= 0:
            print("Please enter a length greater than 0.")
            continue

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Please enter a valid number.")
        continue

    again = input("\nGenerate another password? (y/n): ")

    if again.lower() != "y":
        print("\nThank you for using Password Generator!")
        break
