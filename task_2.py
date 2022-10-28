def get_count_char(str_):
    dict_of_symbols = {}
    if type(str_) is str:
        DEFAULT_COUNT = 0
        str_ = str_.lower()

        if str_:
            for item in str_:
                if item.isalpha():
                    dict_of_symbols[item] = dict_of_symbols.get(item, DEFAULT_COUNT) + 1
            if dict_of_symbols:
                return dict_of_symbols
            else:
                print("В этой строке нет букв")
                return dict_of_symbols
        else:
            print("Это пустая строка")
            return dict_of_symbols
    else:
        print("Это не строка")
        return dict_of_symbols


def percentage(dict_, accuracy=1):
    new_dict = {}
    if type(dict_) is dict:
        if dict_:
            cond = True
            for item in dict_:  # Проверка, что значения в словаре - только числа
                if type(dict_[item]) is not int:
                    cond = False
                    break
            if cond:
                amount = sum(dict_.values())
                for index in dict_:
                    new_dict[index] = round(dict_[index] / amount * 100, accuracy)
                return new_dict
            else:
                print("Значения словаря содержат не только цифры, нельзя найти процентное соотношение символов")
                return new_dict
        else:
            print("Это пустой словарь")
            return new_dict
    else:
        print("Это не словарь")
        return new_dict


var = 2  # тестовые переменные
empty_dict = {}
wrong_dict = {
    'b': "34",
    'a': 5
}
empty_str = ""
wrong_str = "6 ?"

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
count_char = get_count_char(main_str)
print("Количество букв в строчке:", count_char)
print("Процентное соотношение букв в строчке:", percentage(count_char))
