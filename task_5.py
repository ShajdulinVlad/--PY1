import string
import random


def get_random_password(n: int = 8, uniq: bool = False) -> str:  # Второй параметр определеят, будет ли пароль состоять из уникальных символов
    list_of_sym = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits)
    password = random.sample(list_of_sym, n) if uniq else [random.choice(list_of_sym) for _ in range(n)]

    return ''.join(password)


print(get_random_password())
