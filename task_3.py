from random import randint


def get_unique_list_numbers(l_lim: int = -10, u_lim: int = 10, list_size: int = 15) -> list[int]:
    list_of_int = []

    while len(list_of_int) != list_size:
        rand_number = randint(l_lim, u_lim)
        if rand_number not in list_of_int:
            list_of_int.append(rand_number)

    return list_of_int


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
