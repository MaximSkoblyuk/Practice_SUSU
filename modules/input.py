def input_file(file_name: str):
    """Read file"""

    file = open(file_name, 'r')
    input_str = file.read().strip()
    file.close()
    return input_str


if __name__ == '__main__':
    print(input_file('../files/input.txt'))
