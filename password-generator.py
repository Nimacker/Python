import random
import string

def generate_password(length):
    """Generate a random password of the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_passwords(num_passwords, password_length):
    """Generate a list of random passwords of the specified length."""
    passwords = []
    for i in range(num_passwords):
        password = generate_password(password_length)
        passwords.append(password)
    return passwords

def main():
    print('Welcome to Your Password Generator')
    num_passwords = int(input('Amount of Passwords to Generate: '))
    password_length = int(input('Input Your Password Length: '))
    print('\nHere are your passwords:')
    passwords = generate_passwords(num_passwords, password_length)
    for password in passwords:
        print(password)

if __name__ == '__main__':
    main()

