import string
import random


def get_random_password(n: int = 8, uniq: bool = False) -> str:  # Второй параметр определеят, будет ли пароль состоять из уникальных символов
    string_of_sym = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = random.sample(string_of_sym, n) if uniq else [random.choice(string_of_sym) for _ in range(n)]

    return ''.join(password)


print(get_random_password())
