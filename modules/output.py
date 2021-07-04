def output_file(file_name: str, answer: str):
    file = open(file_name, 'w')
    file.write(answer)
    file.close()
    return 0


# output_file('../files/output.txt', 'ACCEPT')
