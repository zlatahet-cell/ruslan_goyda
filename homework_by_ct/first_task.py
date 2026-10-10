import secrets
import string

symbols = string.ascii_letters + string.digits

try:
    length = int(input("Введите длину пароля: "))

except ValueError:
    print("Нужно ввести целое число!")
    exit()

if length <= 0:
    print("Длина должна быть больше нуля!")
    exit()

password = ""
for i in range(length):
    password = password + secrets.choice(symbols)

print("Ваш пароль:", password)