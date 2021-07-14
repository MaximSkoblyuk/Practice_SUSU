def output_file(file_name: str, answer: str):
    """Write to file"""

    file = open(file_name, 'w')
    file.write(answer)
    file.close()
    return 0


if __name__ == '__main__':
    output_file('../files/output.txt', 'ACCEPT')
