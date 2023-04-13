
import random
import string


def generate_password(length):
    """Gennerate a random password of the given length"""
    chars = string.ascii_letters + string.digits + string.punctuation
    password =""
    for i in range(length):
        password += random.choice(chars)
    return password

#example usage: generate a 15-character password
password = generate_password(15)
print(password)