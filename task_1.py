# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

last_number = 15
list_of_numbers = [{'bin': bin(number), 'dec': number,
                    'hex': hex(number), 'oct': oct(number)}
                   for number in range(last_number + 1)]

pprint(list_of_numbers)
