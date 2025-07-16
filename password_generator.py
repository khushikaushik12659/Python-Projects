import random
import string

print(" Welcome to Password Generator!")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("Your secure password is:", password)