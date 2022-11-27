import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_name: str) -> list[dict]:
    list_of_dict = []
    with open(file_name, 'r') as f:
        str_csv = f.read()

    lines_csv = str_csv.split("\n")
    data_ = [line.split(",") for line in lines_csv]
    headers = data_[0]
    values = data_[1:]

    for line in values:
        list_of_dict.append({headers[index]: line[index] for index in range(len(headers))})

    return list_of_dict
    ...  # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
