def input_file(file_name: str):
    file = open(file_name, 'r')
    input_str = file.read().strip()
    file.close()
    return input_str


# print(input_file('../files/input.txt'))
