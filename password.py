import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("暗証番号を何桁にしましょうか。: "))
password = generate_password(length)
print("生成された暗証番号:", password)