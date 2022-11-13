import random


def get_unique_list_numbers() -> list[int]:
    lower_limit = -10
    upper_limit = 10
    size_of_list = 15
    list_of_int = []

    while len(list_of_int) != size_of_list:
        rand_number = random.randint(lower_limit, upper_limit)
        if rand_number not in list_of_int:
            list_of_int.append(rand_number)

    return list_of_int


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
