import random

# Available characters for password
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# Get password length from user
passlen = int(input("Enter the length of password: "))

# Generate password (allows repetition)
password = "".join(random.choices(characters, k=passlen))

print("Generated Password:", password)
