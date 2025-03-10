# Password Generator

This is a simple Python script to generate a **random password** of a user-specified length. It includes a mix of **uppercase letters, lowercase letters, numbers, and special characters** to create a strong and secure password.

## Features
✅ Generates a password of any length specified by the user.  
✅ Includes lowercase and uppercase letters, digits, and special characters.  
✅ Uses `random.choices()` to allow repetition, ensuring better randomness.  
✅ Simple and easy-to-use Python script.

## How to Use
1. Run the script in a Python environment.
2. Enter the desired password length when prompted.
3. The script will generate and display a random password.

## Prerequisites
- Python 3.x installed on your system.

## Running the Script
To run the script, execute the following command in your terminal or command prompt:
```sh
python password_generator.py
```

## Example Output
```
Enter the length of password: 12
Generated Password: K#2gL!9@pY1$
```

## Enhancements (Future Improvements)
- Ensure at least one uppercase, one lowercase, one number, and one special character.
- Add an option to exclude certain characters.
- Improve security by using `secrets` module instead of `random` for cryptographic randomness.

## License
This project is free to use and modify for educational purposes.

