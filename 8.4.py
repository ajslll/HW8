from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice
chars = (ascii_lowercase + ascii_uppercase + digits + punctuation)
symbol_lance = int(input('Введите длину для генерации пароля: '))
password = ''
if symbol_lance >= 9:
    for i in range(symbol_lance):
        password += choice(chars)
    print(f'Пароль: {password}')
else:
    print('Минимальная длина пароля должна быть 9 символов')
